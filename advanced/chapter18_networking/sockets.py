# sockets.py
# Examples and explanations for sockets

import socket

# Simple TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('example.com', 80))
client.sendall(b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n')
response = client.recv(4096)
print('Response:', response)
client.close()
