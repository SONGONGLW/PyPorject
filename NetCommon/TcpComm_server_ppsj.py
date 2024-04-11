# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 18:12:28 2022
@author: SONG

"""
import struct
import socket
import _thread
from time import sleep
import random
from numpy import linspace, sin, pi, power, ceil, log2, arange, random
import numpy as np
from scipy.fftpack import fft, ifft

#通过套接字连接到Google的DNS服务器（8.8.8.8）的80端口。这一步并不会实际发送数据，它只是为了获取本地套接字的IP地址。
def GetHostIP():
    try:
        Socke = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        Socke.connect(('8.8.8.8', 80))
        IP = Socke.getsockname()[0]
    finally:
        Socke.close()
 
    print(IP)
    return IP

def generate_fourier_data(num_samples):
    strs = ""
    # 生成频谱数据
    num_samples = 3000
    # 添加噪声
    noise_power = 5  # 噪声功率
    noise = np.random.normal(scale=np.sqrt(noise_power), size=num_samples)
    noise = noise - 105

    # 指数级递增序列的起始值和终止值
    start_value = -105
    end_value = -70
    # 指数级递增序列的长度
    num_points = 1200
    # 生成从0到1的等间隔序列，作为指数函数的参数
    x = np.linspace(0, 1, num_points)
    # 计算指数级递增序列
    exponential_sequence = start_value + (end_value - start_value) * np.exp(x)
    exponential_sequence = exponential_sequence - 35

    # 截取中间的2400个点
    middle_noise = noise[300:2700] + 105

    #删除点
    noise = noise[:-num_points*2]

    #将序列倒序
    reversed_sequence = exponential_sequence[::-1]

    #合并序列
    exponential_sequence = np.concatenate((exponential_sequence, reversed_sequence))
    
    # 将两个序列中的元素相加
    exponential_sequence = exponential_sequence + middle_noise

    noise = np.insert(noise, 300, exponential_sequence)

    freq = 3000
    i = num_samples
    for value in noise:
        i -= 1
        freq = freq + 0.83
        rounded_freq = round(freq, 3)
        rounded_res = round(value, 3)
        if i != 0:
            strs = strs + str(rounded_freq) + " " + str(rounded_res) + " "
        else:
            strs = strs + str(rounded_freq) + " " + str(rounded_res)

    return strs

def CreateRandom():
    strs = ""
    fourier_data, frequencies = generate_fourier_data(3000)
    i = 3000
    p = 0
    freq = 3000.0
    while i > 0 :
        # res = random.uniform(-120.0, -30.0);
        res = random.uniform(-116.0, -107.0);
        res1 = random.uniform(-84.0, -67.0);
        res2 = random.uniform(-113.0, -110.0);
        res3 = random.uniform(-98.0, -84.0);
        i -= 1
        freq = freq + 0.83
        rounded_freq = round(freq, 2)
        # rounded_res = round(fourier_data[p], 2)

        if (freq> 3500) and (freq < 3600) :
            rounded_res = round(res1, 2)
        elif (freq> 4500) and (freq < 4600) :
            rounded_res = round(res2, 2)
        else:
            rounded_res = round(res, 2)
        p += 1
    
        #hex_res = int_res.to_bytes(2, byteorder='little')
        #strs += hex_res
        if i != 0:
            strs = strs + str(rounded_freq) + " " + str(rounded_res) + " "
        else:
            strs = strs + str(rounded_freq) + " " + str(rounded_res)

    return strs

#数据发送
def send_data(client_socket):
    while client_socket:
        # 3. 从键盘获取数据
        # send_data = b'\x08\x00\x00\x00\x81@\x02\x00\x1d\x00\x00\x00\x10'
        # res = random.uniform(-120.0, -30.0);
        # print( CreateRandom() );
        # send_data = CreateRandom()
        # send_data = inpu("请输入要发送的数据:")
    
        # 4. 发送数据到指定的电脑上的指定程序中 (send_data.encode("gbk"))中文数据
        frame_header = b'\x98\x91'	#帧头
        data = b''
        # strss = CreateRandom()
        strss = generate_fourier_data(3000)
        data = strss.encode()
        data_length = len(data).to_bytes(2, byteorder='little')
        check = b'\x69'
        frame_tail = b'\x98\x92'
        packet = frame_header + data_length + data + check + frame_tail
        client_socket.send(packet)

#接收到的数据
def rece_data(server_socket, client_socket, client_address):
    data = client_socket.recv(1024)
    print("接收到了客户端 %s 传来的数据: %s\n" % (client_address, data))
    print("关闭线程")
    _thread.exit()
    # 关闭套接字
    client_socket.close()
    # server_socket.close()

if __name__ == '__main__':    
        
    # 1. 创建tcp套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP_daar = GetHostIP()
    port = 12353
    dest_addrs = (IP_daar, port)
    server_socket.bind(dest_addrs)
    # 开始监听连接，参数表示最大连接数
    server_socket.listen(5)
    print(f"等待客户端连接在 {IP_daar}:{port} ...")

    while True:
	# 等待客户端连接
        client_socket, client_address = server_socket.accept()
        print(f"接受来自 {client_address} 的连接")

        #数据发送线程
        _thread.start_new_thread(send_data, (client_socket,))
        #数据接收线程
        _thread.start_new_thread(rece_data, (server_socket, client_socket, client_address))
        print("启动线程")
