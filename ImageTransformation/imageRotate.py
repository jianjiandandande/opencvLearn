# _*_ encoding: utf-8 _*_

__author__ = 'Vincent'
__date__ = '2019/3/14 16:35'

import cv2
import numpy as np

# 读取图片的信息
img = cv2.imread('image0.jpg', 1)
cv2.imshow('src', img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]

# 旋转矩阵
matRotate = cv2.getRotationMatrix2D((height*0.5,width*0.5), 45, 0.5) # 1.旋转的中心 2.旋转的角度 3.缩放的系数
dst = cv2.warpAffine(img, matRotate,(width, height))
cv2.imshow('dst', dst)
cv2.waitKey(0)




