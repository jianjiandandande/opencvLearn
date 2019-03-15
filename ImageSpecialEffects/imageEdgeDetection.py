# _*_ encoding: utf-8 _*_

__author__ = 'Vincent'
__date__ = '2019/3/15 16:32'

# 边缘检测
import numpy as np
import cv2
import random
from math import sqrt

'''
 方法一 canny:
  1. gray(灰度处理)
  2. 高斯滤波 -- 去除噪声的干扰 
  3.调用canny API
'''

img = cv2.imread('image0.jpg',1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
cv2.imshow('src',img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgG = cv2.GaussianBlur(gray, (3, 3), 0) # 第二参数为模板的大小,该方法实现滤波功能
dst = cv2.Canny(img,50,50) #后面的两个参数均代表门限 图片经过卷积之后的值如果大于门限，就认为是边缘点
cv2.imshow('dst',dst)
# cv2.waitKey(0)

'''
 方法二 源码的形式实现(sobel算子)
 sobel 1.算子模板 -- 有水平方向和竖直方向两种
       2.图片卷积
       3.阈值判决
    算子模板：
      竖直方向        水平方向
    [ 1   2  1     [ 1  0  -1
      0   0  0       2  0  -2
     -1 -2 -1 ]      1  0  -1 ]
     
    卷积： [1 2 3 4] [a b c d]  结果为：a*1+b*2+c*3+d*4
    通过卷积在水平方向的结果a和竖直方向的结果b进行计算阈值，再与门限进行比较，从而获取
'''

dst2 = np.zeros((height, width, 1), np.uint8)
for i in range(0,height-2):
    for j in range(0, width-2):
        gy = gray[i,j]*1+gray[i,j+1]*2+gray[i,j+2]*1 - gray[i+2, j]*1 - gray[i+2,j+1]*2 - gray[i+2,j+2]*1
        gx = gray[i, j] * 1 + gray[i+1, j] * 2 + gray[i+2, j] * 1 - gray[i, j+2] * 1 - gray[i + 1, j + 2] * 2 - \
             gray[i + 2, j + 2] * 1
        grad = sqrt(gy*gy + gx*gx)
        if grad >50:
            dst2[i,j] = 255
        else:
            dst2[i, j] = 0
cv2.imshow('dst2',dst2)
cv2.waitKey(0)