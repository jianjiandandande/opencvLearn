# _*_ encoding: utf-8 _*_

__author__ = 'Vincent'
__date__ = '2019/3/15 17:47'

# 油画效果
'''
 步骤：
     1.将原图进行灰度化
     2.将原图中每8*8的像素分为1块
     3.将0-255的像素值进行分块，分成8个等级
     4.分别计算第2步中每一块中灰度等级最多的所有像素，并求取像素的均值
     5.用统计出来的平均值来代替原来的像素值
'''

import numpy as np
import cv2
import random
from math import sqrt

img = cv2.imread('image00.jpg',1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
cv2.imshow('src', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dst = np.zeros((height,width,3),np.uint8)
for i in range(4,height-4):
    for j in range(4,width-4):
        array1 = np.zeros(8,np.uint8) # 存储每个等级的个数 将0-255分为8个等级
        for m in range(-4,4):
            for n in range(-4,4):
                p1 = int(gray[i+m,j+n]/32)
                array1[p1] = array1[p1] + 1
        currentMax = array1[0]# 存储各个级别中个数最大值
        l = 0 # 存储最大值所在的级别
        for k in range(0, 8):
            if currentMax < array1[k]:
                currentMax = array1[k]
                l = k
        # 取均值的简化运算
        for m in range(-4,4):
            for n in range(-4,4):
                if gray[i+m, j+n] >= l*32 and gray[i+m, j+n] <= (l+1)*32:
                    (b, g, r) = img[i+m, j+n]
        dst[i, j] = (b, g, r)
cv2.imshow('dst',dst)
cv2.waitKey(0)