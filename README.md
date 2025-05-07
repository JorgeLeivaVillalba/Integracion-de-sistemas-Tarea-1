# Tarea 1

## Requerimientos

Desarrollar un programa en Python que:

1. Lea un archivo CSV de alumnos y cargue registros nuevos en la base de datos SQLite.
   - **Control de no duplicación de registro de alumnos** (10%)
   - **Control de matriculación de curso válido** (10%)
   - **Control de nota no nulo mayor o igual a 0** (10%)
   - **Carga de registros en la base de datos** (20%)

2. Desarrolle otro programa que lea la base de datos y genere 2 archivos:
   - **aplazos.csv**: para alumnos con nota menor a 60 (25%)
   - **aprobados.csv**: para alumnos con nota mayor o igual a 60 (25%)

---

## Estructura de la Base de Datos

### Tabla `alumnos`
- `id`
- `nombre`
- `apellido`
- `fecha_nacimiento`

### Tabla `cursos`
- `id`
- `nombre`

### Tabla `matriculaciones`
- `id`
- `curso_id`
- `alumno_id`
- `anho`
- `nota`




