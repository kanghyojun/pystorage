import readline
import socket

host = "localhost"
port = 7777
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    data = raw_input("pystorage> ")
    s.send(data)
    server_d = s.recv(1024)
    print server_d
    if data == "exit":
        break

readline.redisplay()

s.close()
