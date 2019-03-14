# _*_ encoding: utf-8 _*_

__author__ = 'Vincent'
__date__ = '2019/3/13 18:26'

# 1. load 2. info 3. resize 4.check

import cv2
import numpy as np


img = cv2.imread('image0.jpg',1)
cv2.imshow('src', img)
imgInfo = img.shape
print(imgInfo) # 获取到的是图片的宽度、高度和组成通道
height = imgInfo[0]
width = imgInfo[1]
mode = imgInfo[2]

# 放大 缩小
# 等比例与非等比例


# 等比例
dstHeight = int(height/2)
dstWidth = int(width/2)
# cv 中有四种图片缩放方式 最近领域插值 双线性插值 像素关系重采样立方插值
dst = cv2.resize(img,(dstHeight, dstWidth))
# cv2.imshow('image', dst)
# cv2.waitKey(0)

# 使用位移公式来对图像进行缩放
'''
[[A1 A2 B1],[A3 A4 B2]]
[[A1 A2],[A3 A4]]  [[B1],[B2]]
newX = A1*x + A2*y + B1
newY = A3*x + A4*y + B2
x--->0.5x   A1 = 0.5  A2 = 0  B1 = 0
y--->0.5y   A3 = 0  A4 = 0.5  B2 = 0

'''

matScale = np.float32([[0.5, 0, 0], [0, 0.5, 0]])
dst = cv2.warpAffine(img,matScale,(int(width/2), int(height/2)))
cv2.imshow('dst', dst)
cv2.waitKey(0)
