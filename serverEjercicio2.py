import socket

def procesar_informacion(data):
    # Desglosar la información recibida
    codigo_pais = data[0:2]
    categoria_edad = int(data[2:4])
    genero = data[4]
    fecha_nacimiento = data[5:13]
    nombre_completo = data[13:]

    # Determinar el país
    if codigo_pais == "01":
        pais = "Honduras"
    elif codigo_pais == "02":
        pais = "Costa Rica"
    elif codigo_pais == "03":
        pais = "México"
    # Agregar más condiciones para otros códigos de país
    elif codigo_pais == "00":
        pais = "País Desconocido"
    else:
        pais = "Código de país no reconocido"

    # Determinar la categoría de edad
    if categoria_edad >= 1 and categoria_edad <= 18:
        edad = "menor de edad"
    elif categoria_edad >= 19 and categoria_edad <= 50:
        edad = "adulto"
    else:
        edad = "tercera edad"

    # Construir la respuesta
    respuesta = f"Hola {nombre_completo.replace('-', ' ')}, veo que eres del país de {pais} y tienes {categoria_edad} años, lo que indica que eres {('un niño', 'una niña')[genero == 'F']} {edad}. Sin embargo, al observar tu fecha de nacimiento ({fecha_nacimiento[6:8]}-{fecha_nacimiento[4:6]}-{fecha_nacimiento[0:4]}), noto que la edad no concuerda con la fecha de nacimiento."

    return respuesta

# Configuración del servidor
host = '127.0.0.1'
port = 12345

# Crear el socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print("Servidor escuchando en el puerto:", port)

while True:
    # Aceptar conexiones entrantes
    client_socket, addr = server_socket.accept()
    print('Conexión entrante desde', addr)

    # Recibir datos del cliente
    data = client_socket.recv(1024).decode('utf-8')

    if data:
        # Procesar la información recibida
        respuesta = procesar_informacion(data)

        # Enviar respuesta al cliente
        client_socket.send(respuesta.encode('utf-8'))

    # Cerrar la conexión con el cliente
    client_socket.close()

# Cerrar el socket del servidor
server_socket.close()
