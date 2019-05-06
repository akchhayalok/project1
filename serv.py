#!/usr/bin/python3
import socket
mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
myip=input("Enter the ip address")
mysocket.bind((myip,4448))
mysocket.listen(5)
(client,(ip,port))=mysocket.accept()
mysocket.close()

