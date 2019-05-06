#!/usr/bin/python3

import socket
def localhostinfo():
    h=socket.gethostname()
    n=socket.gethostbyname(h)
    print 
myhostname=socket.gethostname()
print myhostname

