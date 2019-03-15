# _*_ encoding: utf-8 _*_

__author__ = 'Vincent'
__date__ = '2019/3/15 15:07'

import cv2
import numpy as np

# 读取图片的信息
img = cv2.imread('image0.jpg', 1)
cv2.imshow('src', img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
for m in range(100, 300):
    for n in range(100, 200):
        if m % 10 == 0 and n % 10 == 0:
            for i in range(0, 10):
                for j in range(0,10):
                    (b, g, r) = img[m, n]
                    img[m+i, n+j] = (b, g, r)
cv2.imshow('dst', img)
cv2.waitKey(0)
