# _*_ encoding: utf-8 _*_

__author__ = 'Vincent'
__date__ = '2019/3/16 17:24'

import cv2
import numpy as np

img = cv2.imread('image0.jpg', 1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.rectangle(img, (200, 100), (500, 400), (0, 255, 0), 3)
# 4 字体 5 字体的大小
cv2.putText(img,'This is a flow', (100, 300),font, 1, (200, 100, 255), 2, cv2.LINE_AA)
cv2.imshow('src', img)
cv2.waitKey(0)