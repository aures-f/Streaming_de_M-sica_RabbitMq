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


    user = request['user']
    musica = request['musica']


    playlists.setdefault(user, []).append(musica)
    conn.send(json.dumps(playlists[user]).encode())
    conn.close()