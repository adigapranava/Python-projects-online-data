import socket
import sys

def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9998
        s = socket.socket()
    except socket.error as msg:
        print("socket creation error :" + str(msg))

def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the port " + str(port))

        s.bind((host, port))
        s.listen()

    except socket.error as msg:
        print("Socket binding error " + str(msg) + "\n" + "Retrying...")
        bind_socket()

def accept_client():
    conn, address = s.accept()
    print("Connection has been established with: IP:" + str(address[0]) + ' port ' + str(address[1]))
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_responce = str(conn.recv(1024), 'utf-8')
            print(client_responce, end= "")

def main():
    create_socket()
    bind_socket()
    accept_client()
    send_commands()

main()
