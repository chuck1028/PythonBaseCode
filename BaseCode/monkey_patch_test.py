import socket

print(socket.socket)

print("After monkey patch")
from gevent import monkey
monkey.patch_socket()
