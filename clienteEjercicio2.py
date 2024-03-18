# Cliente
import socket
import tkinter as tk

def desglosar_datos(datos):
    codigo_pais = datos[0:2]
    categoria_edad = datos[2:4]
    genero = datos[4]
    fecha_nacimiento = datos[5:13]
    nombre_completo = datos[13:]

    return codigo_pais, categoria_edad, genero, fecha_nacimiento, nombre_completo

def enviar_datos():
    # Obtener los datos de la entrada de texto
    datos_input = datos_entry.get()

    # Desglosar los datos de entrada
    codigo_pais, categoria_edad, genero, fecha_nacimiento, nombre_completo = desglosar_datos(datos_input)

    # Crear el socket
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectar al servidor
    cliente_socket.connect((servidor_host, servidor_puerto))

    # Enviar los datos al servidor
    cliente_socket.send(datos_input.encode('utf-8'))

    # Recibir la respuesta del servidor
    respuesta = cliente_socket.recv(1024).decode('utf-8')

    # Mostrar la respuesta en la etiqueta de resultado
    resultado_label.config(text="Respuesta del servidor: " + respuesta)

    # Cerrar el socket del cliente
    cliente_socket.close()

# Configuración del cliente
servidor_host = '127.0.0.1'
servidor_puerto = 12345

# Crear la ventana
root = tk.Tk()
root.title("Cliente")

# Etiqueta para la entrada de datos
datos_label = tk.Label(root, text="Ingrese los datos:")
datos_label.pack()

# Entrada de texto para los datos
datos_entry = tk.Entry(root)
datos_entry.pack()

# Botón para enviar los datos
enviar_button = tk.Button(root, text="Enviar", command=enviar_datos)
enviar_button.pack()

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(root, text="")
resultado_label.pack()

# Ejecutar la interfaz gráfica
root.mainloop()
