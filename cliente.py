import socket
import tkinter as tk
from tkinter import messagebox

# Envía los datos al servidor
def enviar_datos():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', 9999))

    nombre = entry_nombre.get()
    apellidos = entry_apellidos.get()
    ciudad = entry_ciudad.get()
    edad = entry_edad.get()
    cedula = entry_cedula.get()

    datos = f"{nombre},{apellidos},{ciudad},{edad},{cedula}"
    cliente.send(datos.encode('utf-8'))  

    confirmacion = cliente.recv(1024).decode('utf-8')  
    messagebox.showinfo("Registro", confirmacion)
    cliente.close()

# Muestra los usuarios registrados
def ver_usuarios():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', 9999))
    cliente.send("VER".encode('utf-8'))  # Enviar un comando para obtener los usuarios

    usuarios = cliente.recv(1024).decode('utf-8')  # Recibir la lista de usuarios
    messagebox.showinfo("Usuarios Registrados", usuarios)
    cliente.close()

# Elimina un usuario por cédula
def eliminar_usuario():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', 9999))

    cedula = entry_cedula_eliminar.get()
    cliente.send(f"ELIMINAR,{cedula}".encode('utf-8'))  # Enviar comando para eliminar el usuario

    confirmacion = cliente.recv(1024).decode('utf-8')  # Recibir confirmación
    messagebox.showinfo("Eliminación", confirmacion)
    cliente.close()

# Crea la ventana del cliente
def crear_ventana_cliente():
    ventana = tk.Tk()
    ventana.title("Cliente")
    ventana.geometry("400x500")

    tk.Label(ventana, text="Nombre").pack()
    global entry_nombre
    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack()

    tk.Label(ventana, text="Apellidos").pack()
    global entry_apellidos
    entry_apellidos = tk.Entry(ventana)
    entry_apellidos.pack()

    tk.Label(ventana, text="Ciudad").pack()
    global entry_ciudad
    entry_ciudad = tk.Entry(ventana)
    entry_ciudad.pack()

    tk.Label(ventana, text="Edad").pack()
    global entry_edad
    entry_edad = tk.Entry(ventana)
    entry_edad.pack()

    tk.Label(ventana, text="Cédula (Registro)").pack()
    global entry_cedula
    entry_cedula = tk.Entry(ventana)
    entry_cedula.pack()

    boton_registrar = tk.Button(ventana, text="Registrar", command=enviar_datos)
    boton_registrar.pack()

    tk.Label(ventana, text="Cédula (Eliminar)").pack()
    global entry_cedula_eliminar
    entry_cedula_eliminar = tk.Entry(ventana)
    entry_cedula_eliminar.pack()

    boton_eliminar = tk.Button(ventana, text="Eliminar Usuario", command=eliminar_usuario)
    boton_eliminar.pack()

    boton_ver_usuarios = tk.Button(ventana, text="Ver Usuarios Registrados", command=ver_usuarios)
    boton_ver_usuarios.pack()

    ventana.mainloop()

if __name__ == "__main__":
    crear_ventana_cliente()
