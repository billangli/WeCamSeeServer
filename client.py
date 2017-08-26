"""
client.py
Receive json file from server
Bill Li
Aug. 26th, 2017
"""

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 7878))
client_socket.send('hello'.encode())
