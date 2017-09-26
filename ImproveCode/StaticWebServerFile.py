# -*- coding:utf-8 -*-
# Author: Jason Lee
import re
import socket
from multiprocessing import Process

#设置静态文件根目录
HTML_ROOT_DIR = 'Templates'

def handle_client(client_socket):
    """处理客户端请求"""
    #接收数据
    request_data = client_socket.recv(1024)
    print(request_data)
    request_lines = request_data.splitlines()
    for line in request_lines:
        print(line)
    #解析报文
    request_start_line = request_lines[0]
    #提取用户请求的文件名
    file_name = re.match(r'\w+ +(/[^ ]*) ', request_start_line.decode()).group(1)

    #打开文件，读取内容
    file = open(HTML_ROOT_DIR + file_name, 'rb')
    response_body = file.read()
    file.close()

    #构造响应数据
    response_start_line = 'HTTP/1.1 200 OK\r\n'
    response_headers = 'Server: My server\r\n'

    response = response_start_line + response_headers + '\r\n' + response_body.decode()
    print('response data:', response)
    client_socket.send(bytes(response, 'utf-8'))
    client_socket.close()

if __name__ == '__main__':
    # 新建tcp socket服务端
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('', 8888))
    server_socket.listen(128)

    while True:
        client_socket, client_address = server_socket.accept()
        p = Process(target=handle_client, args=(client_socket,))
        p.start()
        client_socket.close()


