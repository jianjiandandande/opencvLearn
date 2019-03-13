# _*_ encoding: utf-8 _*_

__author__ = 'Vincent'
__date__ = '2019/3/1 11:59'
import cv2

# 图片的写入

img = cv2.imread('image0.jpg',1)# 1.文件的读取 2.封装格式的解析 3.数据解码 4.数据的加载
cv2.imwrite('image1.jpg',img) #1.文件的名称以及格式 2.文件的数据(解码后的)

