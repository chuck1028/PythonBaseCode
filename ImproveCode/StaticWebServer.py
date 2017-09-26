# -*- coding:utf-8 -*-
# Author: Jason Lee
import socket
from multiprocessing import Process

def handle_client(client_socket):
    """处理客户端请求"""
    #接收数据
    request_data = client_socket.recv(1024)
    print(request_data)
    #构造响应数据
    response_start_line = 'HTTP/1.1 200 OK\r\n'
    response_headers = 'Server: My server\r\n'
    response_body = 'hello jason'
    response = response_start_line + response_headers + '\r\n' + response_body
    print('response data:', response)
    client_socket.send(bytes(response, 'utf-8'))
    client_socket.close()

if __name__ == '__main__':
    # 新建tcp socket服务端
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 8003))
    server_socket.listen(128)

    while True:
        client_socket, client_address = server_socket.accept()
        p = Process(target=handle_client, args=(client_socket,))
        p.start()
        client_socket.close()


