import mysql.connector

# Configuración de la conexión a la base de datos MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="agenda2022"
)

# Función para crear la tabla si no existe
def crearTabla():
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contactos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255),
            apellidos VARCHAR(255),
            telefono VARCHAR(20),
            email VARCHAR(255)
        )
    """)
    conexion.commit()
    cursor.close()

# Función para insertar un contacto en la base de datos
def insertar(datos):
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO contactos (nombre, apellidos, telefono, email)
        VALUES (%s, %s, %s, %s)
    """, datos)
    conexion.commit()
    cursor.close()

# Función para consultar todos los contactos
def consultar():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM contactos")
    resultados = cursor.fetchall()
    cursor.close()
    return resultados

# Función para obtener un contacto por su ID
def dameContacto(id):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM contactos WHERE id = %s", (id,))
    resultado = cursor.fetchall()
    cursor.close()
    return resultado

# Función para modificar un contacto
def modificar(id, nombre, apellidos, telefono, email):
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE contactos
        SET nombre = %s, apellidos = %s, telefono = %s, email = %s
        WHERE id = %s
    """, (nombre, apellidos, telefono, email, id))
    conexion.commit()
    cursor.close()

# Función para eliminar un contacto por su ID
def borrar(id):
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM contactos WHERE id = %s", (id,))
    conexion.commit()
    cursor.close()

# Cerrar la conexión cuando termine el programa
def cerrarConexion():
    conexion.close()

# Aquí deberías llamar a la función `crearTabla()` para asegurarte de que la tabla esté creada antes de usarla en otras operaciones

# También deberías llamar a `cerrarConexion()` cuando tu aplicación termine para cerrar la conexión a la base de datos

# Ejemplo de uso:
# crearTabla()  # Llama a esta función para crear la tabla si no existe
# insertar(('Juan', 'Pérez', '123456789', 'juan@example.com'))
# contactos = consultar()
# for contacto in contactos:
#     print(contacto)

# Recuerda reemplazar "tu_host", "tu_usuario", "tu_contraseña" y "nombre_de_tu_base_de_datos"
# con los valores correspondientes de tu configuración MySQL.