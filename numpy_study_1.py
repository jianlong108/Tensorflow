#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

# from matplotlib import pyplot as plt
#
# x = np.arange(1,11)
# y =  2  * x +  5
# plt.title("Matplotlib demo")
# plt.xlabel("x axis caption")
# plt.ylabel("y axis caption")
# plt.plot(x,y)
# plt.show()

# numpy 的版本
print np.version.version

print '=========== 一维数组 ============='

# 以list或tuple变量为参数产生一维数组：
oneDimensionArray = np.array([1, 2, 3, 4])
print oneDimensionArray
print type(oneDimensionArray)

# 以list或tuple变量为元素产生二维数组或者多维数组：
twoDimensionArray = np.array(((1, 2, 3), (4, 5, 6)))
print twoDimensionArray
print type(twoDimensionArray)

# numpy ndarray 元素数据类型可以通过参数dtype 设定
oneDimensionArray_string = np.array(['1.23', '2.34', '3.45'], dtype=np.string_)
print oneDimensionArray_string

# 而且可以使用astype转换类型...
# 注意astype 调用会返回一个新的数组，也就是原始数据的一份拷贝。
oneDimensionArray_float = oneDimensionArray_string.astype(float)
print oneDimensionArray_float

print '一维数组索引: %d' % (oneDimensionArray[1], )

# IndexError: too many indices for array
# print '一维数组索引: %d' % (oneDimensionArray[1,2], )


print '二维数组%s 索引[0,2]值: %d' % (twoDimensionArray, twoDimensionArray[0, 2], )


print twoDimensionArray[1:]
newTwo = twoDimensionArray[:1]
print newTwo

newTwo[0] = 10
newTwo[0, 0] = 11
# newTwo和twoDimensionArray指向是同一块内存空间值，系统没有为newTwo 新开辟空间把x值赋值过去。
print newTwo
print twoDimensionArray


newTwo[0, 0] = 11
print newTwo
print twoDimensionArray


print '----------------'

arr = np.arange(10)

print arr

print arr[4]

print arr[3:6]

arr[3:6] = 12
# 当将一个 常量 赋值给切片时，该值会自动传播整个切片区域.这个跟列表最重要本质区别，
# 数组切片是原始数组的指针，指针上任何修改直接反映到源数据上面。
# 思考为什么这么设计？
# Numpy 设计是为了处理大数据，如果切片采用数据复制话会产生极大的性能和内存消耗问题。
print arr

print '数组的copy----------------'
arr_copy = arr[3:6].copy()

arr_copy[:] = 24

print arr_copy

print arr

print '列表list 切片的修改---------'

temp_l = range(10)

print temp_l

# temp_l[5:8] = 12

temp_l1 = temp_l[5:8]

print temp_l1

temp_l1[0] = 12

print temp_l1

print temp_l



print '=========== 多维数组 ============='

arr2d = np.arange(1, 10).reshape(3, 3)

print arr2d

print arr2d[2]

print arr2d[0][2]

print arr2d[0, 2]

# arr2d = np.arange(0, 10).reshape(1, -1)
# print arr2d

names = np.array(['Bob', 'joe', 'Bob', 'will'])

boolArray = names == 'Bob'
print boolArray
print names

# 在跑实验时经常需要用到读取文件中的数据，其实在numpy中已经有成熟函数封装好了可以使用
# 将数组以二进制形式格式保存到磁盘，np.save 、np.load
# 函数是读写磁盘的两个主要函数，
# 默认情况下，数组以未压缩的原始二进制格式保存在扩展名为.npy的文件中
np.save('~/Users/dalong/Desktop/array', boolArray)
print np.load('array.npy')

np.savetxt('array.txt', boolArray)
print np.loadtxt('array.txt')