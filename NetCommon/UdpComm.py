# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 18:12:28 2022

@author: SONG
"""

import sys
sys.path.extend(['D:\\Anaconda3\\Lib'])
sys.path.extend(['D:\\Anaconda3\\Lib\\site-packages'])
sys.path.extend(['D:\\Anaconda3\\Library\\bin'])
sys.path.extend(['D:\\Anaconda3\\Lib\\site-packages\\partd'])

import socket
import _thread
from time import sleep
import Comm
import random
from numpy import linspace, sin, pi, power, ceil, log2, arange, random
import numpy as np
from scipy.fftpack import fft, ifft

def DrawPlot():
    Fs = 6000 #采样频率
    T = 1/Fs #采样周期，只相邻两数据点的时间间隔
    L = 6000 #信号长度
    t = np.arange(L)*T
    
    noise2 = random.normal(60, 190, Fs)
    
    # while
    S = 1*np.sin(2*np.pi*1200*t) + 1*np.sin(2*np.pi*1210*t)
    X = S + noise2
    
    # plt.plot(t[:50], X[:50])
    # plt.xlabel("Time(s)")
    # plt.ylabel("Amplitude")
    # plt.title("频谱图")
    # plt.show()

    Y = fft(X)
    p2 = np.abs(Y)   # 双侧频谱
    p1 = p2[:int(L/2)]
    f = np.arange(int(L/2))*Fs/L;
    # plt.plot(f, 2*p1/L) 
    # plt.title('频谱图')
    # plt.xlabel('频率MHz')
    # plt.ylabel('功率')
    # plt.show()
    
    lists = 2*p1/L
    lists_new = []
    list_count = 0;
    
    for app_id in lists:
        list_count += 1
        if (list_count >= 800) and (list_count <= 2200):
            if (list_count >= 1000) and (list_count <= 2000):
                lists_new.append(-(app_id + 90))
            else:
                lists_new.append(-(app_id + 45))
        else:
            lists_new.append(-(app_id + 110))
    strsss = " ".join('%s' %a for a in lists_new)   #列表中包含数值需要先将数字转为字符串
    
    return strsss

def GetHostIP():
    try:
        Socke = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        Socke.connect(('8.8.8.8', 80))
        IP = Socke.getsockname()[0]
    finally:
        Socke.close()
 
    print(IP)
    return IP

def CreateRandom():
    strs = ""
    i = 3000;
    while i > 0 :
        res = random.uniform(-120.0, -30.0);
        i -= 1;
        if(i != 0):
            strs = strs + str(res) + " "
        else:
            strs = strs + str(res)
    return strs

#数据发送
def send_data(udp_socket):
    IP_daar = GetHostIP()
    count = 0;
    # 1. 创建udp套接字
    # udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while Comm.flogs == 100:
    # while True:

        # 2. 准备接收方的地址        
        dest_addr = (IP_daar, 8080)  # 注意 是元组，ip是字符串，端口是数字
    
        # 3. 从键盘获取数据
        # send_data = b'\x08\x00\x00\x00\x81@\x02\x00\x1d\x00\x00\x00\x10'
        # res = random.uniform(-120.0, -30.0);
        # print( CreateRandom() );
        # send_data = CreateRandom()
        send_data = DrawPlot()
        
        # send_data = inpu("请输入要发送的数据:")
    
        # 4. 发送数据到指定的电脑上的指定程序中 (send_data.encode("gbk"))中文数据
        udp_socket.sendto(send_data.encode('utf-8'), dest_addr)
        # print("发送给客户端 %s 的数据: %s, count: %s\n" % (dest_addr, send_data, count))
        # sleep(1e-3)
        count += 1

#接收到的数据
def rece_data(udp_socket):
    flogss = True
    while flogss:
        rece_data, client_address = udp_socket.recvfrom(1024)
        print("接收到了客户端 %s 传来的数据: %s\n" % (client_address, rece_data))
        
        flogss = False
        Comm.flogs = 19;
        # 关闭套接字
        udp_socket.close()
        print("关闭线程")
        _thread.exit()


#数据接收
# def receive_data():
#     IP_daar = GetHostIP()
 
#     # 1. 创建udp套接字
#     udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
#     # 2. 准备接收方的地址
#     dest_addr = (IP_daar, 8080)
 
#     # 3. 绑定地址
#     udp_socket.bind(dest_addr)
 
#     while True:
#         # 4. 等待接收对方发送的数据
#         receive_data, client_address = udp_socket.recvfrom(1024)
#         print("接收到了客户端 %s 传来的数据: %s\n" % (client_address, receive_data))
 
#     # 5. 关闭套接字
#     udp_socket.close()

if __name__ == '__main__':    
        
    # 1. 创建udp套接字
    udp_sockets = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    IP_daar = GetHostIP()
    dest_addrs = (IP_daar, 8081)
    udp_sockets.bind(dest_addrs)    

    #数据发送线程
    _thread.start_new_thread(send_data, (udp_sockets,))
    #数据接收线程
    _thread.start_new_thread(rece_data, (udp_sockets,))
    print("启动线程")
    while True:
        sleep(1000)
        i = 0