# _*_ encoding: utf-8 _*_

__author__ = 'Vincent'
__date__ = '2019/3/15 13:27'

# 颜色反转  255 - 当前的像素值

import cv2
import numpy as np

# 读取图片的信息
img = cv2.imread('image0.jpg', 1)
cv2.imshow('src', img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
# 灰度图的反转
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dst = np.zeros((height, width, 1), np.uint8)
for i in range(0, height):
    for j in range(0, width):
        grayPixel = gray[i, j]
        dst[i, j] = 255 - grayPixel
cv2.imshow('dst', dst)
# cv2.waitKey(0)
# 彩色图的反转
dst2 = np.zeros((height, width, 3), np.uint8)
for i in range(0, height):
    for j in range(0, width):
        (b, g, r) = img[i, j]
        dst2[i, j] = (255-b, 255-g, 255-r)
cv2.imshow('dst2', dst2)
cv2.waitKey(0)





