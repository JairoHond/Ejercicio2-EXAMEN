import socket

def procesar_informacion(data):
    codigo_pais = data[0:2]
    categoria_edad = int(data[2:4])
    genero = data[4]
    fecha_nacimiento = data[5:13]
    nombre_completo = data[13:]

    if codigo_pais == "01":
        pais = "Honduras"
    elif codigo_pais == "02":
        pais = "Costa Rica"
    elif codigo_pais == "03":
        pais = "México"
    elif codigo_pais == "00":
        pais = "País Desconocido"
    else:
        pais = "Código de país no reconocido"

    if categoria_edad >= 1 and categoria_edad <= 18:
        edad = "menor de edad"
    elif categoria_edad >= 19 and categoria_edad <= 50:
        edad = "adulto"
    else:
        edad = "tercera edad"

    respuesta = f"Hola {nombre_completo.replace('-', ' ')}, veo que eres del país de {pais} y tienes {categoria_edad} años, lo que indica que eres {('un niño', 'una niña')[genero == 'F']} {edad}. Sin embargo, al observar tu fecha de nacimiento ({fecha_nacimiento[6:8]}-{fecha_nacimiento[4:6]}-{fecha_nacimiento[0:4]}), noto que la edad no concuerda con la fecha de nacimiento."

    return respuesta

host_servidor = '127.0.0.1'
puerto_servidor = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host_servidor, puerto_servidor))
server_socket.listen(1)

print("Servidor escuchando en el puerto:", puerto_servidor)

while True:
    client_socket, addr = server_socket.accept()
    print('Conexión entrante desde', addr)

    data = client_socket.recv(1024).decode('utf-8')

    if data:
        respuesta = procesar_informacion(data)
        client_socket.send(respuesta.encode('utf-8'))

    client_socket.close()

server_socket.close()