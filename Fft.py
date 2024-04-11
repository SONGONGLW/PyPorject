# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 22:06:08 2022

@author: SONG
"""
from time import sleep
import numpy as np
from numpy import linspace, sin, pi, power, ceil, log2, arange, random
from scipy.fftpack import fft, ifft
from matplotlib.pylab import plt

def DrawPlot():
    Fs = 6000 #采样频率
    T = 1/Fs #采样周期，只相邻两数据点的时间间隔
    L = 6000 #信号长度
    t = np.arange(L)*T
    
    noise2 = random.normal(60, 160, Fs)
    
    # while
    S = 80*np.sin(2*np.pi*1200*t) + 80*np.sin(2*np.pi*1210*t)
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
    plt.plot(f, 2*p1/L) 
    plt.title('频谱图')
    plt.xlabel('频率MHz')
    plt.ylabel('功率')
    plt.show()
    
    lists = 2*p1/L
    strsss = " ".join('%s' %a for a in lists)   #列表中包含数值需要先将数字转为字符串
    
    return strsss

print(DrawPlot())    

while True:
    DrawPlot()
    sleep(0.1)
    
# DrawPlot()