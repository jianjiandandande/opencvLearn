# _*_ encoding: utf-8 _*_

__author__ = 'Vincent'
__date__ = '2019/3/25 17:34'

import cv2
import numpy as np
import matplotlib.pyplot as plt



# 灰度图的直方图

img = cv2.imread('image0.jpg', 1)
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
x = np.linspace(0, 255, 256)
y = count
plt.bar(x, y, 0.9, alpha=1, color='b')
plt.show()
# cv2.waitKey(0)

# 彩色图的直方图
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
x = np.linspace(0, 255, 256)
yb = count_b
yg = count_g
yr = count_r
plt.figure()
plt.bar(x, yb, 0.9, alpha=1, color='b')
plt.figure()
plt.bar(x, yg, 0.9, alpha=1, color='g')
plt.figure()
plt.bar(x, yr, 0.9, alpha=1, color='r')
plt.show()
cv2.waitKey(0)
