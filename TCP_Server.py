#! /usr/bin/python3

import socket # Import module

# Create Object = Call function (define family, define type)
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Can just give the IP address. host = '192.168.1.105' etc.
# This automates the getting of host IP address
host = socket.gethostbyname() 
port = 444

serversocket.bind((host, port))

# How many connections will you allow to server.
serversocket.listen(3)

# Loop
while True:
    clientsocket, address = serversocket.accept()
    
    print("received connection from: %s " % str(address))

    message = 'Hello! Thank you for connecting to the server' + "\r\n"
    
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()
