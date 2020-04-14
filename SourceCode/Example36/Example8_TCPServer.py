#!/usr/local/bin/python

# Describe : tcp server

import time
import uuid
import socket
import threading



def dealClient(sock, addr, guid):
    print("Accept new connection from %s:%s..." % addr)
    sock.send(("Hello, I am server = %s!" % guid).encode('utf-8'))

    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        print("-->>%s!" % data.decode('utf-8'))
        sock.send(("Loop_Msg:%s!" % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print("Connection from %s:%s closed" % addr)

def TCPServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1',8888))
    s.listen(5)
    print("Waiting for connection...")
    while True:
        sock,addr = s.accept()
        t = threading.Thread(target=dealClient,
                             args=(sock, addr, uuid.uuid1()))
        t.start()

if __name__ == '__main__':
    TCPServer()
