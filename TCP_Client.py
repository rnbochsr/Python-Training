#! /usr/bin/python3

import socket

# Create socket object. IPv4 & TCP.
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# host = '192.168.1.105' or whatever IP address you need.
host = socket.gethostbyname() # Automates getting host IP.
port = 444

clientsocket.connect((host,port))

message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))
