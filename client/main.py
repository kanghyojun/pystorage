import readline
import socket

host = "localhost"
port = 7777
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    readline.redisplay()
    server_d = s.recv(1024)
    print server_d
    if server_d == "exit server":
        s.close()
        break
    data = raw_input("pystorage> ")
    s.send(data)
