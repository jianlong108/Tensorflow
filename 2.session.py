#!/usr/bin/env python
# -*- coding: utf-8 -*-



import tensorflow as tf
import numpy as np

'''
使用图 (graph) 来表示计算任务.
在被称之为 会话 (Session) 的上下文 (context) 中执行图.
使用 tensor 表示数据.
通过 变量 (Variable) 维护状态.
使用 feed 和 fetch 可以为任意的操作(arbitrary operation) 赋值或者从其中获取数据.


TensorFlow 是一个编程系统, 使用图来表示计算任务.
图中的节点被称之为 op (operation 的缩写). 一个 op 获得 0 个或多个 Tensor, 执行计算, 产生 0 个或多个 Tensor.
 每个 Tensor 是一个类型化的多维数组.
 例如, 你可以将一小组图像集表示为一个四维浮点数数组, 这四个维度分别是 [batch, height, width, channels].

一个 TensorFlow 图描述了计算的过程. 为了进行计算, 图必须在 会话 里被启动.
会话 将图的 op 分发到诸如 CPU 或 GPU 之类的 设备 上, 同时提供执行 op 的方法.
这些方法执行后, 将产生的 tensor 返回.
在 Python 语言中, 返回的 tensor 是 numpy ndarray 对象;
在 C 和 C++ 语言中, 返回的 tensor 是 tensorflow::Tensor 实例.
'''

# 1. 创建一个常量 op, 产生一个 1x2 矩阵. 这个 op 被作为一个节点
# 加到默认图中.
#
# 构造器的返回值代表该常量 op 的返回值.
matrix1 = tf.constant([[3., 3.]])

# 2. 创建另外一个常量 op, 产生一个 2x1 矩阵.
matrix2 = tf.constant([[2.], [2.]])

# 3. 创建一个矩阵乘法 matmul op , 把 'matrix1' 和 'matrix2' 作为输入.
# 返回值 'product' 代表矩阵乘法的结果.
product = tf.matmul(matrix1, matrix2)

'''
默认图现在有三个节点, 两个 constant() op, 和一个matmul() op.
为了真正进行矩阵相乘运算, 并得到矩阵乘法的 结果, 你必须在会话里启动这个图.
'''

# 启动默认图.
sess = tf.Session()

# 调用 sess 的 'run()' 方法来执行矩阵乘法 op, 传入 'product' 作为该方法的参数.
# 上面提到, 'product' 代表了矩阵乘法 op 的输出, 传入它是向方法表明, 我们希望取回
# 矩阵乘法 op 的输出.
#
# 整个执行过程是自动化的, 会话负责传递 op 所需的全部输入. op 通常是并发执行的.
#
# 函数调用 'run(product)' 触发了图中三个 op (两个常量 op 和一个矩阵乘法 op) 的执行.
#
# 返回值 'result' 是一个 numpy `ndarray` 对象.
result = sess.run(product)
print result
# ==> [[ 12.]]

# 任务完成, 关闭会话.
sess.close()