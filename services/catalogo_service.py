import socket
import json


musicas = [
    "Shape of You - Ed Sheeran",
    "Rolling in the Deep - Adele",
    "Smells Like Teen Spirit - Nirvana",
    "Hotel California - Eagles",
    "Uptown Funk - Mark Ronson ft. Bruno Mars",
    "Someone Like You - Adele",
    "Dynamite - BTS",
    "How You Like That - BLACKPINK",
    "LALISA - Lisa",
    "Killin' Me Good - Jihyo",
    "Cupid - FIFTY FIFTY",
    "Next Level - aespa"
]


HOST = 'localhost'
PORT = 5001


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()


print('Serviço de Catálogo ativo...')


while True:
    conn, addr = server.accept()
    data = conn.recv(1024).decode()
    request = json.loads(data)


    if request['action'] == 'buscar':
        conn.send(json.dumps(musicas).encode())


    conn.close()