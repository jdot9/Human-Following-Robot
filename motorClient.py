import socket
import threading
from tests import motorTest as mt
from tests import stepperTest as st

FORMAT = 'ascii'
NAME = 'Pi-2'
colorDetected = False

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 57599))

def receive():
    while True:
        try:
            message = client.recv(1024).decode(FORMAT)
            if message == 'NAME':
                client.send(NAME.encode(FORMAT))
            else:
                colorDetected = colorFound(message)
                mt.moveForward(3)
                print(f"Color detected: {colorDetected}")
        except:
            print("An error occured.")
            client.close()
            break

def colorFound(message):
    if (message == "True"):
        return True
    else:
        return False
    
def follow():
    pass

def write():
    while True:
        message = f'{NAME}: {input("")}'
        client.send(message.encode(FORMAT))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()