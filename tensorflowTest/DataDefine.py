# _*_ encoding: utf-8 _*_

__author__ = 'Vincent'
__date__ = '2019/3/13 15:22'


import tensorflow as tf
data1 = tf.constant(2.5)
data3 = tf.constant(2,dtype=tf.int32)
data2 = tf.Variable(10, name='var')
print(data1) # Tensor("Const:0", shape=(), dtype=float32)
print(data2) # <tf.Variable 'var:0' shape=() dtype=int32_ref>
sess = tf.Session()
print(sess.run(data1))
# tf 中变量的初始化也要在sess中完成
init = tf.global_variables_initializer()
sess.run(init)
print(sess.run(data2))
print(sess.run(data3))
sess.close()
# 本质 tf = tensor + 计算图
# tensor 数据
# operation +-*/ 四则运算  赋值等操作
# 计算图(graphs) 数据操作的过程
# Session 运行环境
# sess使用完之后要进行关闭或者使用with关键字
'''
# with关键字的使用方法：
init = tf.global_variables_initializer()
sess.run(init)
with sess:
    print(sess.run(data1))
    
'''
