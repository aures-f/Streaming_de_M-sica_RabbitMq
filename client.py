import socket
import json


HOST = 'localhost'
PORT = 5000




def send(data):
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(json.dumps(data).encode())
    response = s.recv(1024).decode()
    s.close()
    print('Resposta:', response)




send({'type': 'buscar'})
send({'type': 'playlist', 'user': 'ana', 'musica': 'Imagine'})
send({'type': 'reproduzir', 'user': 'ana', 'musica': 'Imagine'})