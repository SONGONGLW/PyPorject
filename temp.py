# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
    
import Comm    #导入此模块会立即调用此模块的所有函数
import main
from Comm import i as m   #加载模块Comm中的i变量，并且当变量i存在时取别名m

#使用模块内的某个变量
print(m)
print (Comm.i)
print (main.fnum + 10)

i = 1;
while i < 5:
    if(i > 3) : break;
    print (i); i += 1;
    
    
_5_ = 8;
print (i + _5_);

print (type(28))
print (type(True))
print (type(2.8))

#科学计数法
print (2.88e3)  #e表示10的指数，e3 = 10的3次方 2880
print (2880e-3) #e-3即10的-3次方

#复数
print (type(1+2j))
print ((1+2j) + (2+3j))     #虚数单位只能是j或J

#布尔
print (bool(""))
print (bool(" "))
print (bool([]))

#地板除法
print (3 // 2)
print (5 // 2)
print (-5 // 2)

#列表比较
a = [1]
b = [2, 1]
print (a < b)

#





    