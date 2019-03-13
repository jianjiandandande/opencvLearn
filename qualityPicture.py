# _*_ encoding: utf-8 _*_

__author__ = 'Vincent'
__date__ = '2019/3/1 14:38'


# 图片的质量

import cv2

# JPG格式的压缩
img = cv2.imread('image0.jpg',1)
cv2.imwrite('image_quality.jpg',img,[cv2.IMWRITE_JPEG_CHROMA_QUALITY, 0]) # 图片质量的范围：0-100 有损压缩  0 压缩比高


# PNG格式的压缩
# 1.无损压缩
# 2. 透明度设置
img = cv2.imread('image0.jpg',1)
cv2.imwrite('image_quality.png',img,[cv2.IMWRITE_PNG_COMPRESSION, 0])  # 图片质量的范围：0-9   0 压缩比低