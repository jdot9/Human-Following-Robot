import socket
import threading

HOST = socket.gethostbyname('localhost')
PORT = 57599
FORMAT = 'ascii'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
names = []

def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = names[index]
            broadcast(f'{name} disconnected.'.encode(FORMAT))
            names.remove(name)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}.")
        client.send("NAME".encode(FORMAT))
        name = client.recv(1024).decode(FORMAT)
        names.append(name)
        clients.append(client)

        print(f"Name of client: {name}")
        broadcast(f"{name} connected to server.".encode(FORMAT))
        print('')
        #client.send(f"{name} connected to server.".encode(FORMAT))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening...\n")
receive()