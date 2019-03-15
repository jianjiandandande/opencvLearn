# _*_ encoding: utf-8 _*_

__author__ = 'Vincent'
__date__ = '2019/3/15 16:19'

# dst = src1*a + src2*(1-a)

import cv2
import numpy as np

img0 = cv2.imread('image0.jpg',1)
img1 = cv2.imread('image1.jpg',1)
imgInfo0 = img0.shape
# imgInfo1 = img1.shape
height = imgInfo0[0]
width = imgInfo0[1]
# height1 = imgInfo1[0]
# width1 = imgInfo1[1]
# 获取一个感兴趣的范围
roiH = int(height/2)
roiW = int(width/2)
img0ROI = img0[0:roiH, 0:roiW]
img1ROI = img1[0:roiH, 0:roiW]
# dst
dst = np.zeros((roiH,roiW,3), np.uint8)
dst = cv2.addWeighted(img0ROI,0.5,img1ROI,0.5,0)#权重相加 src1*a + src2*(1-a)
cv2.imshow('dst',dst)
cv2.waitKey(0)