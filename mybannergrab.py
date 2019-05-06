#!/usr/bin/python

import socket
sock=socket.socket()
ip_addr=raw_input("Enter ip address")
port=int(input("enter port number"))
sock.connect((ip_addr,port))
print (sock.recv(1024))
sock.close()
