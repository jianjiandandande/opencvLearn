# _*_ encoding: utf-8 _*_

__author__ = 'Vincent'
__date__ = '2019/3/14 14:49'

import cv2


# x  100 ->> 200
# y  100 ->> 300

img = cv2.imread('image0.jpg', 1)
imgInfo = img.shape
dst = img[100:200, 100:300]
cv2.imshow('image_cut', dst)
cv2.waitKey(0)