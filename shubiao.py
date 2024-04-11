import pynput
from time import sleep
import _thread

def kongzhishubiao(x, y):
	shubiao = pynput.mouse.Controller()
	#shubiao.position = (x, y)	#控制鼠标移动到指定位置
	#shubiao.move(x, y)			#移动鼠标
	shubiao.click(pynput.mouse.Button.left)	    #左键单击。
	#shubiao.click(pynput.mouse.Button.left, 2)	 	#左键双击。
	
	#shubiao.scroll(0, 50) #向上滚动50单位。
	#shubiao.scroll(0, -x) #向下滚动x单位。
	
	#shubiao.press(pynput.mouse.Button.left) #按下左键。
	#shubiao.release(pynput.mouse.Button.left) #释放左键。
	
def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if button == pynput.mouse.Button.right:		#当点击的是鼠标右键则结束
        # Stop listener
        return False
		
logs = True
		
def runfunc(num):
	x = 0.01
	y = 20
	while logs:
		kongzhishubiao(x, y)
		sleep(num)
	
if __name__ == '__main__':
	
	snum = input()
	num = float(snum)
	_thread.start_new_thread(runfunc, (num, ))
	
	with pynput.mouse.Listener( on_click = on_click ) as listener: listener.join()
	logs = False
	
	print("结束")
	
	
	
	
	
	
	