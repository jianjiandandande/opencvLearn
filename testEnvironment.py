# _*_ encoding: utf-8 _*_

__author__ = 'Vincent'
__date__ = '2019/3/1 10:24'

import tensorflow as tf
import cv2

hello = tf.constant("hello tf!")
sess = tf.Session()
print(sess.run(hello))

print('hello opencv')