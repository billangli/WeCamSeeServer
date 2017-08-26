"""
server.py
Send json file to client
Bill Li
Aug. 26th, 2017
"""

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 7878))
server_socket.listen(5)

while True:
    connection, address = server_socket.accept()
    buf = connection.recv(64)
    if len(buf) > 0:
        print(buf)
        break
