# _*_ encoding: utf-8 _*_

__author__ = 'Vincent'
__date__ = '2019/3/16 17:24'

import cv2
import numpy as np

img = cv2.imread('image0.jpg', 1)
height = int(img.shape[0]*0.2)
width = int(img.shape[1]*0.2)
newImg = cv2.resize(img,(width, height))
for i in range(0, height):
    for j in range(0, width):
        img[i+200, j+300] = newImg[i, j]

cv2.imshow('src',img)
cv2.waitKey(0)