# _*_ encoding: utf-8 _*_

__author__ = 'Vincent'
__date__ = '2019/3/25 17:11'

import cv2
import numpy as np

# 图片修补
# 1.坏图 2.array描绘图片中坏的部分 3. inpaint

img = cv2.imread('damaged.jpg', 1)
cv2.imshow('src', img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
paint = np.zeros((height, width, 1), np.uint8)
for i in range(200, 300):
    paint[i, 200] = 255
    paint[i, 200 + 1] = 255
    paint[i, 200 - 1] = 255
for i in range(150, 250):
    paint[250, i] = 255
    paint[250 + 1, i] = 255
    paint[250 - 1, i] = 255
cv2.imshow('paint', paint)

# 目标图片
# 1.原图 2. mask(蒙版)
imgDst = cv2.inpaint(img, paint, 3, cv2.INPAINT_TELEA)
cv2.imshow('imgDst', imgDst)
cv2.waitKey(0)
