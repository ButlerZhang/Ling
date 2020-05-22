#!/usr/local/bin/python

# Describe : tcp client


import uuid
import socket


def TCPClient():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 8888))
    print("--->>" + s.recv(1024).decode('utf-8'))
    s.send(("hello, I am a client = %s." % uuid.uuid1()).encode('utf-8'))
    print("--->>" + s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()

if __name__ == '__main__':
    TCPClient()
