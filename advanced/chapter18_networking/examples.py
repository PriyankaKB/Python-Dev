# examples.py
# Example code for networking

import socket
import requests

# Socket example (TCP client)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect(('example.com', 80))
    s.sendall(b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n')
    response = s.recv(1024)
    print('Received:', response)
finally:
    s.close()

# HTTP requests example
response = requests.get('https://api.github.com')
print('Status code:', response.status_code)
print('Headers:', response.headers)
