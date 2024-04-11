# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 17:55:49 2022

@author: SONG
"""

from socket import *

# 创建socket
tcp_client_socket = socket(AF_INET, SOCK_STREAM)

# 目的信息

# 链接服务器
tcp_client_socket.connect(("192.168.0.117", 8234))

# 提示用户输入数据
send_data = "请输入要发送的数据："

tcp_client_socket.send(send_data.encode("gbk"))

# 接收对方发送过来的数据，最大接收1024个字节
recvData = tcp_client_socket.recv(1024)
print('接收到的数据为:', recvData.decode('gbk'))

# 关闭套接字
tcp_client_socket.close()

