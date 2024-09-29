EXPLICACIÓN DEL CÓDIGO 

 

En el archivo servidor.py el código crea un servidor básico de red que gestiona el registro, la visualización y la eliminación de usuarios en una base de datos SQLite, utilizando sockets para la comunicación con los clientes. A continuación, se explica paso a paso: 

1. Inicialización de la base de datos 

La función inicializar_base_datos se ejecuta al inicio para crear una base de datos usuarios.db si no existe y define la tabla usuarios con las siguientes columnas: 

id: Identificador único para cada usuario, autoincremental. 

nombre: Nombre del usuario. 

apellidos: Apellidos del usuario. 

ciudad: Ciudad del usuario. 

edad: Edad del usuario. 

cedula: Número único de cédula, el cual no se puede repetir (definido como UNIQUE). 

 

 

 

2. Registro de usuarios 

La función registrar_usuario se encarga de insertar un nuevo usuario en la base de datos, validando que la cédula no esté registrada previamente. Si la cédula ya existe, lanza una excepción sqlite3.IntegrityError, devolviendo un mensaje de error. 

 

 

 

 

 

3. Obtener usuarios 

La función obtener_usuarios selecciona todos los usuarios de la base de datos y los retorna en formato de texto, listando los datos como nombre, apellidos, ciudad, edad y cédula. 

 

4. Eliminar un usuario 

La función eliminar_usuario elimina un usuario de la base de datos en función de su cédula. 

 

 

5. Manejo de clientes 

La función manejar_cliente es la encargada de recibir solicitudes de los clientes. Dependiendo del tipo de mensaje recibido, realiza las siguientes acciones: 

Si el mensaje es "VER", llama a la función obtener_usuarios y envía la lista de usuarios de vuelta al cliente. 

Si el mensaje comienza con "ELIMINAR", extrae la cédula, elimina el usuario y envía una confirmación. 

Para cualquier otro mensaje, se espera que contenga los datos del usuario en formato nombre, apellidos, ciudad, edad, cedula, y se registra el nuevo usuario llamando a registrar_usuario. 

 

 

6. Inicio del servidor 

 

La función iniciar_servidor inicializa el servidor utilizando la biblioteca socket. Realiza lo siguiente: 

Crea un socket con socket.AF_INET (IPv4) y socket.SOCK_STREAM (TCP). 

Asocia el socket a la dirección localhost y el puerto 9999. 

El servidor queda en modo "escucha" (con la función listen) esperando conexiones de clientes. 

Cuando un cliente se conecta, el servidor acepta la conexión y crea un nuevo hilo para gestionar las solicitudes de ese cliente sin bloquear la atención de otras conexiones. 

 

 

 

En el archivo cliente.py el código define una interfaz gráfica de usuario (GUI) utilizando la biblioteca Tkinter para interactuar con un servidor mediante sockets. A continuación, te explico paso a paso cada parte del código de este archivo de cliente: 

1. Librerías Importadas 

socket: Proporciona las funciones necesarias para crear una conexión cliente-servidor utilizando sockets TCP. 

tkinter: Es el módulo estándar para crear interfaces gráficas en Python. 

messagebox: Se utiliza para mostrar cuadros de diálogo emergentes (pop-ups) con mensajes de información, error, etc. 

 

2. Función enviar_datos() 

2.1 Crea un socket del lado del cliente y se conecta al servidor en el puerto 9999 del localhost. 

 

 

2.2 Obtiene los valores de las entradas de texto (nombre, apellidos, ciudad, edad, cédula) y los convierte en una cadena separada por comas para enviarla al servidor. 

 

 

 

 

2.3 Espera la confirmación del servidor sobre el éxito o el fallo del registro y la muestra en un cuadro de diálogo emergente. Luego, cierra la conexión con el servidor. 

 

 

3. Función ver_usuarios() 

3.1 Esta función conecta al servidor y envía el comando "VER" para solicitar la lista de usuarios registrados. 

 

 

3.2 Recibe la lista de usuarios registrados, la decodifica y la muestra en un cuadro de diálogo. Finalmente, cierra la conexión. 

 

 

4. Función eliminar_usuario() 

4.1 Esta función obtiene el número de cédula ingresado en el campo correspondiente, se conecta al servidor y envía el comando "ELIMINAR" junto con la cédula. 

 

4.2 Recibe una confirmación del servidor sobre si el usuario fue eliminado o no, la muestra en un cuadro de diálogo, y cierra la conexión. 

 

 

5. Función crear_ventana_cliente() 

5.1 Esta función define la ventana principal del cliente con Tkinter: 

Crea la ventana principal con un título "Cliente" y un tamaño de 400x500 píxeles. 

 

 

5.2 Se crean las etiquetas ("Label") y los campos de entrada ("Entry") para nombre, apellidos, ciudad, edad, y cédula. Cada campo es empacado con el método pack(), que los coloca uno debajo del otro. 

 

 

5.3 Se añade un botón para registrar usuarios que al ser presionado llama a la función enviar_datos(). 

 

 

5.4 Se añade una sección con un campo para ingresar la cédula que será eliminada y un botón que llama a la función eliminar_usuario(). 

 

5.5 Se añade un botón adicional que llama a ver_usuarios() para mostrar todos los usuarios registrados. 

 

5.6 El método mainloop() inicia el bucle de eventos de la ventana para que la interfaz gráfica se mantenga abierta y responda a las interacciones del usuario. 

 

 

6. Ejecución del Cliente 

6.1 Finalmente, si este archivo es ejecutado directamente, llama a la función crear_ventana_cliente() para abrir la interfaz gráfica. 

 

 

Este código crea una interfaz gráfica que permite a un usuario interactuar con un servidor a través de tres funciones: registrar un usuario, ver la lista de usuarios y eliminar un usuario, todo a través de sockets TCP. 
