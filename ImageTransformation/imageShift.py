# _*_ encoding: utf-8 _*_

__author__ = 'Vincent'
__date__ = '2019/3/14 15:10'

import cv2
import numpy as np

# 读取图片的信息
img = cv2.imread('image0.jpg', 1)
cv2.imshow('src',img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]

'''
API方式
'''

'''
    移位矩阵：
    [[1, 0, 100], [0, 1, 200]] 2*3---》2*2  2*1
    [[1, 0], [0, 1]] 2*2  A
    [[100],[200]] 2*1  B
    xy  C
    A*C+B = XY  [[1*x+0*y],[0*x+1*y]] + [[100],[200]] = [[x+100],[y+200]]
    
'''
matShift = np.float32([[1, 0, 100], [0, 1, 200]]) # 2X3
dst = cv2.warpAffine(img,matShift,(width, height)) # 1.data 2.移位矩阵matShfit 3.info
cv2.imshow('dst', dst)
cv2.waitKey(0)

'''
源代码方式
 newX = x+100   newY = y+200
'''

dst2 = np.zeros(img.shape, np.uint8)

for i in range(0,int(height) - 200):
    for j in range(0, int(width) - 100):
       dst2[i+200, j+100] = img[i, j]
# cv2.imshow('dst2',dst2)
# cv2.waitKey(0)