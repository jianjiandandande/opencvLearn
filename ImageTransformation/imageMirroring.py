# _*_ encoding: utf-8 _*_

__author__ = 'Vincent'
__date__ = '2019/3/14 15:36'

import cv2
import numpy as np

# 读取图片的信息
img = cv2.imread('image0.jpg', 1)
cv2.imshow('src', img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
deep = imgInfo[2]

newImageInfo = (height*2, width, deep)
dst = np.zeros(newImageInfo, np.uint8)
for i in range(0,int(height)):
    for j in range(0, int(width)):
        dst[i, j] = img[i, j]
        # x不变 y=2*height-y -1
        dst[height*2-i-1, j] = img[i, j]
for i in range(0,width):
    dst[height,i] = (0, 0, 255)#BGR
cv2.imshow('dst', dst)
cv2.waitKey(0)
