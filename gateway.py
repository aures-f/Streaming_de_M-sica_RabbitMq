import socket
import json
from messaging import publish


HOST = 'localhost'
PORT = 5000


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()


print('Gateway ativo...')


while True:
    conn, addr = server.accept()
    data = conn.recv(1024).decode()
    request = json.loads(data)


    if request['type'] == 'buscar':
        s = socket.socket()
        s.connect((HOST, 5001))
        s.send(json.dumps({'action': 'buscar'}).encode())
        response = s.recv(1024).decode()
        s.close()
        conn.send(response.encode())


    elif request['type'] == 'playlist':
        s = socket.socket()
        s.connect((HOST, 5002))
        s.send(json.dumps(request).encode())
        response = s.recv(1024).decode()
        s.close()
        conn.send(response.encode())


    elif request['type'] == 'reproduzir':
        publish('historico', request)
        conn.send(json.dumps({'status': 'evento enviado'}).encode())
    
    elif request['type'] in ['playlist', 'ver_playlist']:
        s = socket.socket()
        s.connect(('localhost', 5002))
        s.send(json.dumps(request).encode())
        resp = s.recv(4096).decode()
        s.close()
        conn.send(resp.encode())



    conn.close()