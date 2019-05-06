#!/usr/bin/python3
import socket
mysoc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
myip=input("enter ip address")
myport=int(input("enter port number"))
mysoc.bind((myip,myport))
mysoc.listen(5)
((myconn,myaddress))=mysoc.accept()
myconn.send(b"hello this a server")
mysoc.close()
