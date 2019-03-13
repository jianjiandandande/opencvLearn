# _*_ encoding: utf-8 _*_

__author__ = 'Vincent'
__date__ = '2019/3/13 14:45'

'''
  像素：图片放大之后会看到一个个的方块 ，每一个方块都是像素
  RGB 每种颜色都由RGB三种分量来进行组合
  颜色深度：8bit 0-255 对于8bit 的RGB图片来说它可以表示256^3种颜色
  图片的宽高 w h 640 * 480 宽 640个像素点 高 480个像素点
  alpha 透明度
  颜色存储格式 RGB bgr
  
  
  图片坐标系中 ，x==图片的列 ， y==图片的行
'''

import cv2
img = cv2.imread('image0.jpg',1)
