import socket
import json

HOST = 'localhost'
PORT = 5000

def send(data):
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(json.dumps(data).encode())
    response = s.recv(4096).decode()
    s.close()
    print('\nResposta:', response)

while True:
    print("\n=== CLIENTE STREAMING ===")
    print("1 - Listar músicas (Catálogo)")
    print("2 - Adicionar à playlist")
    print("3 - Reproduzir música")
    print("4 - Ver playlist do usuário")
    print("0 - Sair")

    op = input("Escolha uma opção: ")

    if op == "1":
        send({'type': 'buscar'})

    elif op == "2":
        user = input("Usuário: ")
        musica = input("Música: ")
        send({'type': 'playlist', 'user': user, 'musica': musica})

    elif op == "3":
        user = input("Usuário: ")
        musica = input("Música: ")
        send({'type': 'reproduzir', 'user': user, 'musica': musica})

    elif op == "4":
        user = input("Usuário: ")
        send({'type': 'ver_playlist', 'user': user})

    elif op == "0":
        print("Encerrando cliente...")
        break

    else:
        print("Opção inválida!")
