# -*- coding:utf-8 -*-
# Author: Jason Lee
import select
import socket
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 7788))
server.listen(5)

inputs = [server]

running = True

while True:
    #第一个参数：检测列表中的套接字是否可以收数据
    #第二个参数：检测列表中的套接字是否可以发数据
    #第三个参数：检测列表中的套接字是否发生了异常
    readable, writeable, execptional = select.select(inputs, [], [])
    for sock in readable:
        #监听到新的连接
        if sock == server:
            conn, addr = server.accept()
            inputs.append(conn)
        #监听到键盘有输入
        elif sock == sys.stdin:
            cmd = sys.stdin.readline()
            running = False
            break
        #监听到有数据到来
        else:
            data = sock.recv(1024)
            if data:
                sock.send(data)
            else:
                inputs.remove(sock)
                sock.close()






