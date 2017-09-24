# -*- coding:utf-8 -*-
# Author: Jason Lee
import sys
import time
import gevent

from gevent import socket, monkey
monkey.patch_all()    #放在文件开头，相当于打补丁，可以标记当前文件的IO操作

def handle_request(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            conn.close()
            break
        print('data')
        conn.send(data)

def server(port):
    s = socket.socket()
    s.bind('', port)
    s.listen(5)

    while True:
        cli, addr = s.accept()
        gevent.spawn(handle_request, cli)

if __name__ == '__main__':
    server(7788)