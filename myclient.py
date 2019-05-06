#!/usr/bin/python3
import socket
mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.connect(("192.168.1.10",4448))
mysocket.close


