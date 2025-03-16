import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *
import mysql.connector
from mysql.connector import Error

# Configuración de conexión MySQL
config = {
    'user': 'tu_usuario',
    'password': 'tu_contraseña',
    'host': 'localhost',
    'database': 'videojuego'
}

def conectar():
    try:
        conn = mysql.connector.connect(**config)
        if conn.is_connected():
            return conn
    except Error as e:
        print(f'Error de conexión: {e}')
        return None

class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        self.name = ""
        self.score = 0
        self.start_game = False
        self.font = pg.font.Font(None, 48)
        self.is_game_over = False

    def draw_start_screen(self):
        """Pantalla de inicio para ingresar el nombre."""
        self.screen.fill('black')
        title = self.font.render("DOOM Style Game", True, (255, 255, 255))
        prompt = self.font.render("Ingresa tu nombre:", True, (255, 255, 255))
        name_text = self.font.render(self.name, True, (0, 255, 0))
        start_text = self.font.render("Presiona Enter para comenzar", True, (255, 255, 255))

        self.screen.blit(title, (400 - title.get_width() // 2, 150))
        self.screen.blit(prompt, (400 - prompt.get_width() // 2, 250))
        self.screen.blit(name_text, (400 - name_text.get_width() // 2, 350))
        self.screen.blit(start_text, (400 - start_text.get_width() // 2, 450))
        pg.display.flip()

    def check_start_events(self):
        """Eventos de la pantalla de inicio."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN and self.name.strip():
                    self.register_player()
                    self.start_game = True
                elif event.key == pg.K_BACKSPACE:
                    self.name = self.name[:-1]
                else:
                    self.name += event.unicode

    def register_player(self):
        """Registrar al jugador en la base de datos."""
        conn = conectar()
        if conn:
            try:
                cursor = conn.cursor()
                query = "INSERT INTO jugadores (nombre, puntuacion) VALUES (%s, %s)"
                valores = (self.name, self.score)
                cursor.execute(query, valores)
                conn.commit()
            except Error as e:
                print(f'Error al registrar jugador: {e}')
            finally:
                cursor.close()
                conn.close()

    def start_screen(self):
        """Manejar el inicio del juego."""
        while not self.start_game:
            self.check_start_events()
            self.draw_start_screen()

    def update_score_in_db(self):
        """Actualizar la puntuación al morir."""
        conn = conectar()
        if conn:
            try:
                cursor = conn.cursor()
                query = "UPDATE jugadores SET puntuacion = %s WHERE nombre = %s"
                valores = (self.score, self.name)
                cursor.execute(query, valores)
                conn.commit()
            except Error as e:
                print(f'Error al actualizar puntuación: {e}')
            finally:
                cursor.close()
                conn.close()

    def new_game(self):
        """Inicializar el juego."""
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)
        pg.mixer.music.play(-1)

    def update(self):
        """Actualizar lógica del juego."""
        if not self.is_game_over:
            self.player.update()
            self.raycasting.update()
            self.object_handler.update()
            self.weapon.update()
            self.delta_time = self.clock.tick(FPS)

    def draw(self):
        """Dibujar elementos en pantalla."""
        self.screen.fill('gray')
        self.object_renderer.draw()
        self.weapon.draw()

        # Mostrar la puntuación abajo a la derecha
        score_text = self.font.render(f"Puntos: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (self.screen.get_width() - score_text.get_width() - 20, self.screen.get_height() - 50))

        pg.display.flip()

    def game_over(self):
        """Finalizar el juego."""
        self.is_game_over = True
        self.update_score_in_db()
        self.screen.fill('black')
        game_over_text = self.font.render("¡Fin del juego!", True, (255, 0, 0))
        final_score_text = self.font.render(f"Puntuación final: {self.score}", True, (255, 255, 255))
        self.screen.blit(game_over_text, (400 - game_over_text.get_width() // 2, 250))
        self.screen.blit(final_score_text, (400 - final_score_text.get_width() // 2, 350))
        pg.display.flip()
        pg.time.wait(3000)
        pg.quit()
        sys.exit()

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.game_over()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)
    


    def run(self):
        """Iniciar el flujo del juego."""
        self.start_screen()
        self.new_game()
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()