import random
import cv2
import numpy as np
 
def cal(point,here):
    # 计算樱花中的坐标在屏幕中投影的坐标
    # here不断增大，delta不断减少
    delta = point[0] - here
    if delta==0:
        return [-1, -1, 1, 0, 0]
    x = point[1]/delta   # 投影在屏幕上x坐标
    y = point[2]/delta   # 投影在屏幕上y坐标
    r = point[3]/delta   # 星球半径
    return [x, y, r]
 
def display_all(sakura,here):
      result=[]
      for i in range(sakura_num):
            position = cal(sakura[i],here)
            result.append(position)
      return result
 
if __name__ == "__main__":
     height=800
     width=1600
     step = 0.5
     min_r = 1
     max_r = 200
     sakura_num = 150
     x_far = 100*2
     y_far = width*x_far
     z_far = height*x_far
     here = 0
     sakura = [[0,0,0,0,0] for i in range(sakura_num)]
     cv2.namedWindow('sakura',0)
     while True:
           canvas=np.zeros((height,width,3),dtype=np.uint8)
           here+=step
           for i in range(sakura_num):
                  while True:
                          position = cal(sakura[i],here)
                          if (0 <= position[0] < width and
                              0 <= position[1] < height and sakura[i][0]>here):
                              break
                          else:
                              sakura[i][0] = random.randint(x_far, 2*x_far)+here
                              sakura[i][1] = random.randint(0, 2*y_far)
                              sakura[i][2] = random.randint(0, 2*z_far)
                              sakura[i][3] = random.randint(min_r, max_r)
           result=display_all(sakura,here)
           result=np.uint16(result).tolist()
           for i in range(sakura_num):
                radius=np.random.randint(3,15,size=(1,2)).tolist()[0]
                cv2.ellipse(canvas,tuple(result[i][0:2]),tuple(radius),30,0,360,color=(233,192,255),thickness = -1)
           cv2.imshow('sakura',canvas)
           if cv2.waitKey(10)==27:
               cv2.destroyAllWindows()
               break