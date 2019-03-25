# _*_ encoding: utf-8 _*_

__author__ = 'Vincent'
__date__ = '2019/3/25 20:53'

# 磨皮美白


import cv2
import numpy as np

img = cv2.imread('1.png', 1)
# cv2.imshow('src', img)
# cv2.waitKey(0)
## 双边滤波
dst = cv2.bilateralFilter(img, 15, 35, 35)
# cv2.imshow('dst', dst)
# cv2.waitKey(0)

## 高斯滤波

imgGa = cv2.imread('image11.jpg', 1)
# cv2.imshow('Gu', imgGa)

dstGa = cv2.GaussianBlur(imgGa, (5, 5), 1.5)
# cv2.imshow('dstGa', dstGa)
# cv2.waitKey(0)

## 均值滤波 [6, 6]的全1矩阵 * [6, 6]的图像矩阵  = [6, 6]/36 得到均值  然后用均值替换掉中心元素的像素值

imgMe = cv2.imread('image11.jpg')
imgInfo = imgMe.shape
height = imgInfo[0]
width = imgInfo[1]
# cv2.imshow('src', imgMe)
dstMe = np.zeros((height, width, 3), np.uint8)
for i in range(3, height - 3):
    for j in range(3, width - 3):
        sum_b = int(0)
        sum_g = int(0)
        sum_r = int(0)
        for m in range(-3, 3):
            for n in range(-3, 3):
                (b, g, r) = imgMe[i + m, j + n]
                sum_b = sum_b + int(b)
                sum_g = sum_g + int(g)
                sum_r = sum_r + int(r)
        b = np.uint8(sum_b / 36)
        g = np.uint8(sum_g / 36)
        r = np.uint8(sum_r / 36)
        dstMe[i, j] = (b, g, r)
# cv2.imshow('dstMe', dstMe)
# cv2.waitKey(0)

## 中值滤波  使用3*3矩阵中间的像素值代替其他像素值的过程
imgMedium = cv2.imread('image11.jpg')
imgInfo = imgMedium.shape
height = imgInfo[0]
width = imgInfo[1]
# cv2.imshow('src', imgMedium)
grayMedium = cv2.cvtColor(imgMedium, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', grayMedium)
dstMedium = np.zeros((height,width, 3), np.uint8)
collect = np.zeros(9, np.uint8)
for i in range(1, height-1):
    for j in range(1, width-1):
        k = 0
        for m in range(-1, 2):
            for n in range(-1, 2):
                gray = grayMedium[i, j]
                collect[k] = gray
                k = k + 1
        for k in range(0, 9):
            p1 = collect[k]
            for t in range(k+1,9):
                if p1<collect[t]:
                    mid = collect[t]
                    collect[t] = p1
                    p1 = mid
        dstMedium[i, j] = collect[4]
cv2.imshow('dstMedium', dstMedium)
cv2.waitKey(0)