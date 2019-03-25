# _*_ encoding: utf-8 _*_

__author__ = 'Vincent'
__date__ = '2019/3/25 20:10'

'''
    直方图的均衡化：
      1.计算每一个灰度等级的概率
      2.计算累计概率
      3.计算映射表
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 灰度图的直方图均衡化

img = cv2.imread('image0.jpg', 1)
cv2.imshow('src', img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# count 用来记录像素值在其对应的灰度等级下出现的概率
count = np.zeros(256, np.float)  # 256个灰度等级
for i in range(0, height):
    for j in range(0, width):
        pixel = gray[i, j]
        index = int(pixel)
        count[index] = count[index] + 1
for i in range(0, 256):
    count[i] = count[i] / (height * width)
# 计算累计概率
sum = float(0)
for i in range(0, 256):
    sum = sum + count[i]
    count[i] = sum
# 计算映射表
map = np.zeros(256, np.uint16)
for i in range(0,256):
    map[i] = np.uint16(count[i]*255)
for i in range(0, height):
    for j in range(0, width):
        pixel = gray[i, j]
        gray[i, j] = map[pixel]
cv2.imshow('dst', gray)
# cv2.waitKey(0)

# 彩色图的直方图均衡化
# 统计概率
count_b = np.zeros(256, np.float)  # 256个灰度等级
count_g = np.zeros(256, np.float)  # 256个灰度等级
count_r = np.zeros(256, np.float)  # 256个灰度等级
for i in range(0, height):
    for j in range(0, width):
        (b, g, r) = img[i, j]
        index_b = int(b)
        index_g = int(g)
        index_r = int(r)
        count_b[index_b] = count_b[index_b] + 1
        count_g[index_g] = count_g[index_g] + 1
        count_r[index_r] = count_r[index_r] + 1
for i in range(0, 256):
    count_b[i] = count_b[i] / (height * width)
    count_g[i] = count_g[i] / (height * width)
    count_r[i] = count_r[i] / (height * width)
# 计算累计概率
sum_b = float(0)
sum_g = float(0)
sum_r = float(0)
for i in range(0, 256):
    sum_b = sum_b + count_b[i]
    count_b[i] = sum_b
    sum_g = sum_g + count_g[i]
    count_g[i] = sum_g
    sum_r = sum_r + count_r[i]
    count_r[i] = sum_r

# 计算映射关系
map_b = np.zeros(256, np.uint16)
map_g = np.zeros(256, np.uint16)
map_r = np.zeros(256, np.uint16)
for i in range(0,256):
    map_b[i] = np.uint16(count_b[i]*255)
    map_g[i] = np.uint16(count_g[i]*255)
    map_r[i] = np.uint16(count_r[i]*255)
dst = np.zeros((height, width, 3), np.uint8)
for i in range(0, height):
    for j in range(0, width):
        (b, g, r) = img[i, j]
        b = map_b[b]
        g = map_g[g]
        r = map_r[r]
        dst[i, j] = (b, g, r)
cv2.imshow('dst', dst)
cv2.waitKey(0)