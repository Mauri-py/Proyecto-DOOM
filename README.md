# 🎮 **DOOM REMAKE - Python Edition** 🔥  

¡Bienvenido al remake de DOOM hecho en **Python**! ⚡  
Un solo nivel, acción infinita y registro de puntajes en **MySQL**.  

---

## 🚀 **Características**
✅ Remake de DOOM programado en Python.  
✅ Un solo nivel infinito: ¡resistí todo lo que puedas!  
✅ Base de datos **MySQL** para registrar puntajes de **2 jugadores**.  
✅ 🎯 Enfréntate a hordas de enemigos y supera tu récord.  

🎮 **[ESPACIO PARA UNA IMAGEN DEL JUEGO]**  

---

## 📚 **Instalación y Configuración**

### 🔹 **1. Clona el Repositorio**
```bash
git clone https://github.com/tu-usuario/doom-remake.git
cd doom-remake
```

### 🔹 **2. Instala las Dependencias**
```bash
pip install -r requirements.txt
```

### 🔹 **3. Configura la Base de Datos**
1. Asegurate de tener **MySQL** instalado y en ejecución.  
2. Crea la base de datos y la tabla con el siguiente script SQL:  

```sql
CREATE DATABASE videojuego;
USE videojuego;

CREATE TABLE jugadores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    puntuacion INT
);
```

3. Edita el archivo `config.py` con tus credenciales de MySQL.  

---

## 🎮 **Cómo Jugar**
🔸 Ejecuta el juego con:  
```bash
python main.py
```
🔸 En la pantalla de inicio, ingresa tu nombre y presiona **Enter**.  
🔸 Usa **WASD** para moverte.  
🔸 Apunta y dispara con el **mouse**.  
🔸 ¡Sobrevive el mayor tiempo posible!  

🎮 **[ESPACIO PARA UNA IMAGEN DEL GAMEPLAY]**  

---

## 🏆 **Registro de Puntajes**
- Al iniciar, el juego registra tu nombre en la base de datos.  
- Al morir, tu **puntuación final se guarda** en MySQL.  
- Puedes consultar los **2 mejores puntajes** con:  

```sql
SELECT * FROM jugadores ORDER BY puntuacion DESC LIMIT 2;
```

---

## 💻 **Tecnologías Utilizadas**
- 🐍 **Python**
- 🎥 **Pygame** (motor gráfico)
- 📄 **MySQL** (almacenamiento de puntajes)
- ⚙ **SQLAlchemy** (para la conexión con la DB)  

---

## 📌 **Créditos**
🔹 Proyecto desarrollado por **[Tu Nombre o Alias]**.  
🔹 Basado en el clásico **DOOM** de id Software.  

Si te gustó, ¡no olvides darle una ⭐ en el repo! 🦌🔥  

---

🎮 **[ESPACIO PARA UNA ÚLTIMA IMAGEN ÉPICA]**  
