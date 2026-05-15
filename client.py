import socket
import threading
from datetime import datetime

host = '127.0.0.1'
port = 5555

nickname = input("Enter your name: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# Receive messages
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')

            if message == "NICK":
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("Error!")
            client.close()
            break
# Send messages
def write():
       while True:
            message = input("")
            print("\033[A                             \033[A")

            time = datetime.now().strftime("%H:%M")
            full_msg = f"[{time}] {nickname}: {message}"
            client.send(full_msg.encode('utf-8'))
           
threading.Thread(target=receive).start()
threading.Thread(target=write).start()