# _*_ encoding: utf-8 _*_

__author__ = 'Vincent'
__date__ = '2019/3/15 15:38'


import cv2
import numpy as np
import random

# 读取图片的信息
img = cv2.imread('image0.jpg', 1)
cv2.imshow('src', img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
dst = np.zeros((height, width, 3), np.uint8)
mm = 8 #随机范围

for m in range(0, height - mm):
    for n in range(0, width - mm):
        index = int(random.random()*8)
        (b, g, r) = img[m+index, n+index]
        dst[m, n] = (b, g, r)

cv2.imshow('dst',dst)
cv2.waitKey(0)

