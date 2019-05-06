#!/usr/bin/python3
import socket
mysoc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysoc.connect(("192.168.1.10",4447))
data=mysoc.recv(2048)
print(data)
