import sqlite3
import socket
import threading

# Inicializa la base de datos
def inicializar_base_datos():
    conexion = sqlite3.connect('usuarios.db')
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        apellidos TEXT NOT NULL,
                        ciudad TEXT NOT NULL,
                        edad INTEGER NOT NULL,
                        cedula TEXT NOT NULL UNIQUE)''')
    conexion.commit()
    conexion.close()

# Registra un nuevo usuario
def registrar_usuario(nombre, apellidos, ciudad, edad, cedula):
    conexion = sqlite3.connect('usuarios.db')
    cursor = conexion.cursor()
    try:
        cursor.execute('''INSERT INTO usuarios (nombre, apellidos, ciudad, edad, cedula) 
                          VALUES (?, ?, ?, ?, ?)''', (nombre, apellidos, ciudad, edad, cedula))
        conexion.commit()
        return "Usuario registrado correctamente."
    except sqlite3.IntegrityError:
        return "Error: La cédula ya está registrada."
    finally:
        conexion.close()

# Obtiene todos los usuarios registrados
def obtener_usuarios():
    conexion = sqlite3.connect('usuarios.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, apellidos, ciudad, edad, cedula FROM usuarios")
    usuarios = cursor.fetchall()
    conexion.close()
    
    if usuarios:
        return "\n".join([f"{u[0]} {u[1]}, Ciudad: {u[2]}, Edad: {u[3]}, Cédula: {u[4]}" for u in usuarios])
    else:
        return "No hay usuarios registrados."

# Elimina un usuario por cédula
def eliminar_usuario(cedula):
    conexion = sqlite3.connect('usuarios.db')
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM usuarios WHERE cedula = ?", (cedula,))
    conexion.commit()
    conexion.close()

# Maneja la conexión con el cliente
def manejar_cliente(cliente_socket):
    datos = cliente_socket.recv(1024).decode('utf-8')
    
    if datos == "VER":
        usuarios = obtener_usuarios()
        cliente_socket.send(usuarios.encode('utf-8'))
    elif datos.startswith("ELIMINAR"):
        cedula = datos.split(",")[1]
        eliminar_usuario(cedula)
        cliente_socket.send(f"Usuario con cédula {cedula} eliminado.".encode('utf-8'))
    else:
        nombre, apellidos, ciudad, edad, cedula = datos.split(',')
        resultado = registrar_usuario(nombre, apellidos, ciudad, edad, cedula)
        cliente_socket.send(resultado.encode('utf-8'))

# Inicia el servidor
def iniciar_servidor():
    inicializar_base_datos()
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('localhost', 9999))
    servidor.listen(5)  
    print("Servidor iniciado y esperando conexiones...")

    while True:
        cliente_socket, direccion = servidor.accept()  
        print(f"Conexión establecida con {direccion}")
        threading.Thread(target=manejar_cliente, args=(cliente_socket,)).start()

if __name__ == "__main__":
    iniciar_servidor()
