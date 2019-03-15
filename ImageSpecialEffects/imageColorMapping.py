# _*_ encoding: utf-8 _*_

__author__ = 'Vincent'
__date__ = '2019/3/15 17:37'

# 颜色映射  rgb --->  RGB
# b = b*1.5
# g = g*1.3

import cv2
import numpy as np

# 读取图片的信息
img = cv2.imread('image0.jpg', 1)
cv2.imshow('src', img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
dst = np.zeros((height,width,3),np.uint8)
for i in range(0,height):
    for j in range(0, width):
        (b, g, r) = img[i, j]
        b = b * 1.5
        g = g * 1.3
        if b > 255:
            b = 255
        if g > 255:
            g = 255
        dst[i, j] = (b, g, r)
cv2.imshow('dst', dst)
cv2.waitKey(0)
