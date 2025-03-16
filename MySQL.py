import mysql.connector
from mysql.connector import Error

# Configura la conexión a la base de datos
config = {
    'user': 'tu_usuario',  # Reemplaza 'tu_usuario' con tu usuario de MySQL
    'password': 'tu_contraseña',  # Reemplaza 'tu_contraseña' con tu contraseña de MySQL
    'host': 'localhost',
    'database': 'videojuego'
}

def conectar():
    """Establecer la conexión a la base de datos."""
    try:
        conn = mysql.connector.connect(**config)
        if conn.is_connected():
            print('Conexión exitosa a la base de datos')
            return conn
    except Error as e:
        print(f'Error: {e}')
    return None

def insertar_jugador(nombre, puntuacion):
    """Insertar un nuevo jugador en la tabla."""
    conn = conectar()
    if conn:
        try:
            # Usar `with` para gestionar el cursor de manera automática
            with conn.cursor() as cursor:
                query = "INSERT INTO jugadores (nombre, puntuacion) VALUES (%s, %s)"
                valores = (nombre, puntuacion)
                cursor.execute(query, valores)
                conn.commit()
                print('Datos insertados correctamente')
        except Error as e:
            print(f'Error: {e}')
        finally:
            conn.close()  # Cerramos la conexión, el cursor se cierra automáticamente

def obtener_jugadores():
    """Obtener y mostrar todos los jugadores de la tabla."""
    conn = conectar()
    if conn:
        try:
            # Usar `with` para gestionar el cursor de manera automática
            with conn.cursor() as cursor:
                query = "SELECT nombre, puntuacion FROM jugadores"
                cursor.execute(query)
                for (nombre, puntuacion) in cursor:
                    print(f'Nombre: {nombre}, Puntuación: {puntuacion}')
        except Error as e:
            print(f'Error: {e}')
        finally:
            conn.close()  # Cerramos la conexión, el cursor se cierra automáticamente

# Ejemplo de uso
insertar_jugador('Jugador1', 1000)
insertar_jugador('Jugador2', 1500)
obtener_jugadores()