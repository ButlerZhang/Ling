#!/usr/local/bin/python

# Describe : UDP server


import socket

UDPPort = 7777

def UDPServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('127.0.0.1', UDPPort))
    print("Bind UDP on " + str(UDPPort))
    while True:
        data, addr = s.recvfrom(1024)
        print("Received from %s:%s." % addr, data)
        s.sendto(b"Hello, %s!" % data, addr)



def UDPClient():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for data in [b'Hello', b'World']:
        s.sendto(data, ('127.0.0.1', UDPPort))
        print(s.recv(1024).decode('utf-8'))
    s.close()


def TestUDP():
    print("Select: 0 is Server, 1 is Client:")
    select = int(input())
    if select == 0:
        UDPServer()
    else:
        UDPClient()

if __name__ == '__main__':
    TestUDP()