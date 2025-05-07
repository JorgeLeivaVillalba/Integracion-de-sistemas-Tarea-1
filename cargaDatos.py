import sqlite3
import csv

#  verificar si un alumno ya existe
def alumno_existe(cursor, alumno_id):
    cursor.execute("SELECT id FROM alumnos WHERE id = ?", (alumno_id,))
    return cursor.fetchone() is not None

#  carga desde el  CSV
def cargar_datos(csv_file, db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            alumno_id = int(row['alumno_id'])
            nombre = row['nombre']
            apellido = row['apellido']
            fecha_nacimiento = row['fecha_nacimiento']
            curso_id = int(row['curso_id'])
            anho = int(row['anho'])
            nota = int(row['nota'])

            # Control de no duplicación de registro de alumnos
            if not alumno_existe(cursor, alumno_id):
                cursor.execute('''INSERT INTO alumnos (id, nombre, apellido, fecha_nacimiento)
                                  VALUES (?, ?, ?, ?)''', (alumno_id, nombre, apellido, fecha_nacimiento))

            # Control de nota no nulo y mayor o igual a 0
            if nota <= 0:
                print(f"Nota inválida: {nota}")
                continue

            # Insertar matriculación
            cursor.execute('''INSERT INTO matriculaciones (curso_id, alumno_id, anho, nota)
                              VALUES (?, ?, ?, ?)''', (curso_id, alumno_id, anho, nota))

    conn.commit()
    conn.close()
    print("Datos cargados!")

# Ejecutar la carga de datos
if __name__ == "__main__":
    cargar_datos('datos.csv', 'universidad.db')