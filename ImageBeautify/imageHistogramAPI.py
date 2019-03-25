# _*_ encoding: utf-8 _*_

__author__ = 'Vincent'
__date__ = '2019/3/25 16:22'

# 直方图的本质：展示图片中每个像素灰度 出现的概率 0-255 纵坐标 p(概率)
import cv2
import numpy as np
def ImageHist(image, type):
    color = (255, 255, 255)
    windomName = 'Gray'
    if type == 31:#b
        color = (255, 0, 0)
        windomName = 'B Hist'
    elif type == 32:#g
        color = (0, 255, 0)
        windomName = 'G Hist'
    elif type == 33:#r
        color = (0, 0, 255)
        windomName = 'R Hist'
    # 完成直方图的统计 1.img 2计算直方图的通道，这里只有一个通道[0]
    # 3.mask蒙版  4.直方图中size分成多少份 5.直方图中各个像素的值
    hist = cv2.calcHist([image],[0], None, [256], [0.0, 255.0])
    # 获取直方图中的最大值、最小值、以及最大值与最小值所对应的下标 以方便进行归一化
    minV,maxV,minL,maxL = cv2.minMaxLoc(hist)
    # 创建一个画布
    histImg = np.zeros([256, 256, 3], np.uint8)
    # 在画布中绘制
    for h in range(256):
        # 归一化数据
        intenNormal = int(hist[h]*256/maxV)
        cv2.line(histImg, (h, 256), (h, 256-intenNormal),color)
    cv2.imshow(windomName, histImg)
    return histImg

img = cv2.imread('image0.jpg', 1)
channels = cv2.split(img)#RGB - R G B
for i in range(0, 3):
    ImageHist(channels[i], 31+i)
cv2.waitKey(0)