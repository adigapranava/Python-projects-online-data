import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
SERVER = "157.45.215.11"
ADDR = (SERVER, PORT)
DISCONNECT_MSG = "disconnect"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length =str(msg_length).encode(FORMAT)
    client.send(send_length)
    client.send(message)

msg=input()
send(msg)
