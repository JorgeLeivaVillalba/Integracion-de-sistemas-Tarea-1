import sqlite3
import csv

def exportar_datos(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # alumnos con nota menor a 6 (aplazos)
    cursor.execute('''
        SELECT alumnos.id, alumnos.nombre, alumnos.apellido, matriculaciones.nota
        FROM matriculaciones
        INNER JOIN alumnos ON matriculaciones.alumno_id = alumnos.id
        WHERE matriculaciones.nota < 6
    ''')
    aplazos = cursor.fetchall()

    # alumnos con nota mayor o igual a 6 (aprobados)
    cursor.execute('''
        SELECT alumnos.id, alumnos.nombre, alumnos.apellido, matriculaciones.nota
        FROM matriculaciones
        INNER JOIN alumnos ON matriculaciones.alumno_id = alumnos.id
        WHERE matriculaciones.nota >= 6
    ''')
    aprobados = cursor.fetchall()

    # Exportar aplazos.csv
    with open('aplazos.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['alumno_id', 'nombre', 'apellido', 'nota'])  # Encabezado
        writer.writerows(aplazos)

    # Exportar aprobados.csv
    with open('aprobados.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['alumno_id', 'nombre', 'apellido', 'nota'])  # Encabezado
        writer.writerows(aprobados)

    conn.close()
    print("Archivos generados !")


if __name__ == "__main__":
    exportar_datos('universidad.db')