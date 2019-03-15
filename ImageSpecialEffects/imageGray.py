# _*_ encoding: utf-8 _*_

__author__ = 'Vincent'
__date__ = '2019/3/14 16:59'


import cv2
import numpy as np
# 灰度图片默认的深度为1 彩色的为3

# 方法一：imread

img = cv2.imread('image0.jpg', 0) # 0为灰度图，1为彩色图
cv2.imshow('dst1', img)
# cv2.waitKey(0)

# 方法二：cvtColor方法

img1 = cv2.imread('image0.jpg', 1)
dst = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) #1.原始数据  2.转换的模式
cv2.imshow('dst2', dst)
# cv2.waitKey(0)


# 方法三：灰度图片的RGB三通道的值是相等的

img2 = cv2.imread('image0.jpg',1)
imageInfo = img2.shape
height = imageInfo[0]
width = imageInfo[1]
dst = np.zeros((height,width,3), np.uint8)
for i in range(0,height):
    for j in range(0,width):
        (b, g, r) = img2[i,j]
        gray = (int(b)+int(g)+int(r))/3
        dst[i,j] = np.uint8(gray) # 灰度图只有1通道
cv2.imshow('dst3',dst)
# cv2.waitKey(0)

# 方法四： gray = r*0.299+g*0.587+b*0.114(心理学计算方法)
img4 = cv2.imread('image0.jpg',1)
imageInfo4 = img4.shape
height4 = imageInfo4[0]
width4 = imageInfo4[1]
dst4 = np.zeros((height4, width4, 1), np.uint8)
for i in range(0, height4):
    for j in range(0, width4):
        (b, g, r) = img2[i, j]
        gray = int(r)*0.299+int(g)*0.587+int(b)*0.114
        dst4[i, j] = np.uint8(gray) # 灰度图只有1通道
cv2.imshow('dst4', dst4)
cv2.waitKey(0)