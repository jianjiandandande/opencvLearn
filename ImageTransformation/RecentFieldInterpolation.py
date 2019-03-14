# _*_ encoding: utf-8 _*_

__author__ = 'Vincent'
__date__ = '2019/3/14 14:37'

import cv2
import numpy as np

'''
最近领域插值：
 src 10*20  dst 5*10
 目标图像dst上的点全部来源于原图像src
 (1,2)  <----  (2,4)
 dst上的x (1)--> 对应 src 上的点newX (2)  
 newX = x*(src 行/ dst 行)
 newY = y*(src 列/ dst 列)
 如果计算得到的值不为整数，那么可以将其映射到与该值相邻比较近的整数上 12.3 -->  12


'''
img = cv2.imread('image0.jpg', 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
dstHeight = int(height/2)
dstWidth = int(width/2)
dstImage = np.zeros((dstHeight, dstWidth, 3), np.uint8) #0-255
for i in range(0, dstHeight):
    for j in range(0, dstWidth):
        iNew = int(i*(height*1.0/dstHeight))
        jNew = int(j*(width*1.0/dstWidth))
        dstImage[i][j] = img[iNew][jNew]

cv2.imshow("RecentFieldInterpolationImage", dstImage)
cv2.waitKey(0)