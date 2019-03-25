# _*_ encoding: utf-8 _*_

__author__ = 'Vincent'
__date__ = '2019/3/25 16:55'

# 灰度 直方图均衡化

import cv2
import numpy as np
img = cv2.imread('image0.jpg', 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('src', gray)
dst = cv2.equalizeHist(gray)
cv2.imshow('dst', dst)
# cv2.waitKey(0)

# 彩色图 直方图均衡化
cv2.imshow('src-color', img)
# 在使用直方图均衡化的时候要对一种通道进行处理
(b, g, r) = cv2.split(img)# 通道分解
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)
result = cv2.merge((bH, gH, rH)) # 通道合成
cv2.imshow('dst-color', result)
# cv2.waitKey(0)

# YUV 直方图均衡化
imgYUV = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
cv2.imshow('YUV', imgYUV)
channelYUV = cv2.split(imgYUV)
channelYUV[0] = cv2.equalizeHist(channelYUV[0])
channelYUV[1] = cv2.equalizeHist(channelYUV[1])
channelYUV[2] = cv2.equalizeHist(channelYUV[2])
channels = cv2.merge(channelYUV)
result = cv2.cvtColor(channels, cv2.COLOR_YCrCb2BGR)
cv2.imshow('dst-YUV', result)
cv2.waitKey(0)