import numpy as np
import matplotlib.pyplot as plt
import _thread
from time import sleep

def DrawPlot():
    
    while True:
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

        sleep(0.1)

        plt.cla()
        plt.plot(noise)
        plt.draw()
        print("qidong")

    

if __name__ == '__main__':    
        
    
    plt.title('Time domain signal with noise')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')

    
    

    #画图线程
    _thread.start_new_thread(DrawPlot,)
    print("启动线程")

    plt.show()