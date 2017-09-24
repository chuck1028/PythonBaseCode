# -*- coding:utf-8 -*-
# Author: Jason Lee
import socket
import select

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(('', 7788))

s.listen(5)

epoll = select.epoll()

epoll.register(s.fileno(), select.EPOLLIN|select.EPOLLET)

connections = {}
addresses = {}

while True:
    #epoll进行fd扫描的地方 -- 未指定超时时间则为阻塞等待
    epoll_list = epoll.poll()
    for fd, events in epoll_list:
        if fd == s.fileno():
            conn, addr = s.accept()
            connections[conn.fileno()] = conn
            addresses[conn.fileno()] = addr

            epoll.register(conn.fileno(), select.EPOLLIN|select.EPOLLET)

        #EPOLLIN(可读)
        #EPOLLOUT(可写)
        #EPOLLET(ET模式，边缘触发) --> LT为水平触发
        elif events == select.EPOLLIN:
            recvData = connections[fd].recv(1024)
            if len(recvData) > 0:
                print(recvData)
            else:
                epoll.unregister(fd)
                connections[fd].close()





