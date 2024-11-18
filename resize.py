import cv2
import numpy as np
import math
image1=cv2.imread("jangle1+.jpg")
image3=cv2.imread("jangle1+.jpg")
print(image3.shape)

h=image1.shape[0]
w=image1.shape[1]


new_h=math.floor(h/3)
new_w=math.floor(w/3)
img2=np.zeros(shape=(new_w,new_h,3),dtype=np.uint8)

for y in range(new_h):
      for x in range(new_w):
       img2[y][x][2]=image3[math.floor(y*3)][math.floor(x*3)][2]
       img2[y][x][1]=image3[math.floor(y*3)][math.floor(x*3)][1]
       img2[y][x][0]=image3[math.floor(y*3)][math.floor(x*3)][0]


cv2.imshow("1",image1)
cv2.imshow("2",img2)
cv2.waitKey(0)   
