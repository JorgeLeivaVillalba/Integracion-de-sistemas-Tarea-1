import sqlite3
import random
from datetime import datetime, timedelta

# Crear conexión a la base de datos
conn = sqlite3.connect('universidad.db')
cursor = conn.cursor()

# Crear tabla alumnos
cursor.execute('''CREATE TABLE IF NOT EXISTS alumnos
              (id INTEGER PRIMARY KEY,
               nombre TEXT,
               apellido TEXT,
               fecha_nacimiento DATE)''')

# Crear tabla cursos
cursor.execute('''CREATE TABLE IF NOT EXISTS cursos
              (id INTEGER PRIMARY KEY,
               nombre TEXT)''')

# Crear tabla matriculaciones
cursor.execute('''CREATE TABLE IF NOT EXISTS matriculaciones
              (id INTEGER PRIMARY KEY,
               curso_id INTEGER,
               alumno_id INTEGER,
               anho INTEGER,
               nota INTEGER,
               FOREIGN KEY(curso_id) REFERENCES cursos(id),
               FOREIGN KEY(alumno_id) REFERENCES alumnos(id))''')

conn.commit()
conn.close()

print("Base de datos creada y datos dummy generados correctamente.")
