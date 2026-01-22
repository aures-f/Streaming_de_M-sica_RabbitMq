import socket
import json

playlists = {}

HOST = 'localhost'
PORT = 5002

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print('Serviço de Playlist ativo...')

while True:
    conn, addr = server.accept()
    data = conn.recv(1024).decode()
    request = json.loads(data)

    tipo = request.get('type')

    if tipo == 'playlist':
        user = request['user']
        musica = request['musica']
        playlists.setdefault(user, []).append(musica)
        resposta = {"status": "ok", "playlist": playlists[user]}

    elif tipo == 'ver_playlist':
        user = request['user']
        resposta = {"playlist": playlists.get(user, [])}

    else:
        resposta = {"erro": "tipo inválido"}

    conn.send(json.dumps(resposta).encode())
    conn.close()
