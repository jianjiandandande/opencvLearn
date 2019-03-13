# _*_ encoding: utf-8 _*_

__author__ = 'Vincent'
__date__ = '2019/3/1 10:57'

## 图片的显示
import cv2
img = cv2.imread('image0.jpg',1)#图片的读取，1 name 2{0:gray,1:color}
cv2.imshow('image',img)
cv2.waitKey(0)#暂停