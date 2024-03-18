import socket
import tkinter as tk

def desglosar_cadena(cadena):
    codigo_pais = cadena[0:2]
    categoria_edad = cadena[2:4]
    genero = cadena[4]
    fecha_nacimiento = cadena[5:13]
    nombre_completo = cadena[13:]

    return codigo_pais, categoria_edad, genero, fecha_nacimiento, nombre_completo

def enviar_cadena():
    # Obtener la cadena de entrada desde la entrada de texto
    cadena_input = cadena_entry.get()

    # Desglosar la cadena de entrada
    codigo_pais, categoria_edad, genero, fecha_nacimiento, nombre_completo = desglosar_cadena(cadena_input)

    # Crear el socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectar al servidor
    client_socket.connect((host, port))

    # Enviar la cadena al servidor
    client_socket.send(cadena_input.encode('utf-8'))

    # Recibir la respuesta del servidor
    respuesta = client_socket.recv(1024).decode('utf-8')

    # Mostrar la respuesta en la etiqueta de resultado
    resultado_label.config(text="Respuesta del servidor: " + respuesta)

    # Cerrar el socket del cliente
    client_socket.close()

# Configuración del cliente
host = '127.0.0.1'
port = 12345

# Crear la ventana
root = tk.Tk()
root.title("Cliente")

# Etiqueta para la entrada de cadena
cadena_label = tk.Label(root, text="Ingrese la cadena:")
cadena_label.pack()

# Entrada de texto para la cadena
cadena_entry = tk.Entry(root)
cadena_entry.pack()

# Botón para enviar la cadena
enviar_button = tk.Button(root, text="Enviar", command=enviar_cadena)
enviar_button.pack()

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(root, text="")
resultado_label.pack()

# Ejecutar la interfaz gráfica
root.mainloop()
