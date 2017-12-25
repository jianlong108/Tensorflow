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

# np.save('array', boolArray)
# print np.load('array.npy')
#
# np.savetxt('array.txt', boolArray)
# print np.loadtxt('array.txt')


print '=========== Ndarray对象 ============='

'''
object 任何暴露数组接口方法的对象都会返回一个数组或任何序列
dtype  数组的所需数据类型，可选。
copy   可选，默认为true，对象是否被复制。
order  C(按行)、F(按列)或A(任意，默认)。
subok  默认情况下，返回的数组被强制为基类数组。 如果为true，则返回子类。
ndimin 指定返回数组的最小维数。
'''
# def array(p_object, dtype=None, copy=True, order=None, subok=False, ndmin=0)

# 1. dtype 参数
str_a = np.array([1, 2, 3], dtype=str)
print str_a

ndmin_a = np.array([1, 2, 3, 4, 5, 6], ndmin=3)
print ndmin_a

# ndarray 对象由计算机内存中的一维连续区域组成，带有将每个元素映射到内存块中某个位置的索引方案。
# 内存块以按行(C 风格)或按列(FORTRAN 或 MatLab 风格)的方式保存元素。

print '=========== NumPy数组属性 ============='
# ndarray.shape 返回一个包含数组维度的元组，它也可以用于调整数组大小。
a = np.array([[1, 2, 3], [4, 5, 6]])
print 'a = np.array([[1, 2, 3], [4, 5, 6]]) 的维度:%s' % (a.shape ,)

'''
shape是将数组本身的维度改变.reshape改变维度后返回一个新的数组,原来数组不变
'''
# a.shape = (3, 2)
# print a

a.shape = (1, 3, 2)
print 'a.shape(1, 3, 2) 后 a为:\n %s\n' % (a, )


# b是新返回的数组. 2行 3列
b = a.reshape(2, 3)

print 'b = a.reshape(2, 3) 后 a为:\n %s' % (a, )
print 'b = a.reshape(2, 3) 后 b为:\n %s' % (b, )


# a和b的维度都是2维
print 'a的维度%d b的维度%d\n' % (a.ndim, b.ndim)

'''
def arange(start=None, stop=None, step=None, dtype=None)

start 开始值
stop  结束值
step  等差值 默认为1
dtype 指定数据类型
'''
one_D_arr = np.arange(0, 24, 3)
print 'np.arange(0, 24, 3) == %s\n' % (one_D_arr, )

print 'np.arange(24) == %s\n' % (np.arange(24), )

'''
每个维度乘积应为数组的原始大小
reshape(2,3,4) 数组reshape为一个3维数组.
3维数组包含2个二维数组,一个二维数组包含3个一维数组,一个一维数组包含4个元素
'''
three_D_arr = np.arange(24).reshape(2, 3, 4)
print 'three_D_arr ==\n %s\n' % (three_D_arr, )

'''
numpy.itemsize
元素为最小单元 元素的字节长度
这一数组属性返回数组中每个元素的字节单位长度。
'''
print 'three_D_arr.每个元素的单位长度 %d' % (three_D_arr.itemsize, )

a = np.arange(6, dtype=np.int8)
print a.itemsize
a.shape = (2, 3)
print a.itemsize

'''
ndarray对象拥有以下属性。这个函数返回了它们的当前值。

序号	属性及描述
1.	C_CONTIGUOUS (C) 数组位于单一的、C 风格的连续区段内
2.	F_CONTIGUOUS (F) 数组位于单一的、Fortran 风格的连续区段内
3.	OWNDATA (O) 数组的内存从其它对象处借用
4.	WRITEABLE (W) 数据区域可写入。 将它设置为flase会锁定数据，使其只读
5.	ALIGNED (A) 数据和任何元素会为硬件适当对齐
6.	UPDATEIFCOPY (U) 这个数组是另一数组的副本。当这个数组释放时，源数组会由这个数组中的元素更新
'''
print a.flags


print '==============numpy.的初始化数组==============='
'''
numpy.empty(shape, dtype = float, order = 'C')
序号	参数及描述
1.	Shape 空数组的形状，整数或整数元组
2.	Dtype 所需的输出数组类型，可选
3.	Order 'C'为按行的 C 风格数组，'F'为按列的 Fortran 风格数组
'''
empty_arr = np.empty([2, 3], dtype=int)
print '未初始化的空数组:\n%s\n' % (empty_arr, )

'''
numpy.zeros
返回特定大小，以 0 填充的新数组。

numpy.zeros(shape, dtype = float, order = 'C')
序号	参数及描述
1.	Shape 空数组的形状，整数或整数元组
2.	Dtype 所需的输出数组类型，可选
3.	Order 'C'为按行的 C 风格数组，'F'为按列的 Fortran 风格数组
'''

zero_arr = np.zeros((2, 3))
print '特定大小，以 0 填充的新数组:\n%s\n' % (zero_arr,)

one_arr = np.ones((2, 3))
print '特定大小，以 1 填充的新数组:\n%s\n' % (one_arr,)

'''
此函数类似于numpy.array，除了它有较少的参数。 这个例程对于将 Python 序列转换为ndarray非常有用。

numpy.asarray(a, dtype = None, order = None)
序号	参数及描述
1.	a 任意形式的输入参数，比如列表、列表的元组、元组、元组的元组、元组的列表
2.	dtype 通常，输入数据的类型会应用到返回的ndarray
3.	order 'C'为按行的 C 风格数组，'F'为按列的 Fortran 风格数组
'''
x = [1, 2, 3]
a = np.asarray(x)
print type(x), a, type(a)

a = np.asarray(x, dtype=float)
print a

# 元祖作为参数
y = (4, 5, 6)
print np.asarray(y)

'''
numpy.frombuffer
此函数将缓冲区解释为一维数组。 暴露缓冲区接口的任何对象都用作参数来返回ndarray。

numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)

序号	参数及描述
1.	buffer 任何暴露缓冲区借口的对象
2.	dtype 返回数组的数据类型，默认为float
3.	count 需要读取的数据数量，默认为-1，读取所有数据
4.	offset 需要读取的起始位置，默认为0
'''
s =  'Hello,World'
a = np.frombuffer(s, dtype='S1')
print a

'''
此函数从任何可迭代对象构建一个ndarray对象，返回一个新的一维数组。

numpy.fromiter(iterable, dtype, count = -1)

序号	参数及描述
1.	iterable 任何可迭代对象
2.	dtype 返回数组的数据类型
3.	count 需要读取的数据数量，默认为-1，读取所有数据
'''

list = range(5)
print list, type(list)

print np.asarray(list)
print np.fromiter(iter(list), dtype=float)

'''
numpy.linspace
此函数类似于arange()函数。 在此函数中，指定了范围之间的均匀间隔数量，而不是步长。 此函数的用法如下。

numpy.linspace(start, stop, num, endpoint, retstep, dtype)
构造器接受下列参数：

序号	参数及描述
1.	start 序列的起始值
2.	stop 序列的终止值，如果endpoint为true，该值包含于序列中
3.	num 要生成的等间隔样例数量，默认为50
4.	endpoint 序列中是否包含stop值，默认为ture
5.	retstep 如果为true，返回样例，以及连续数字之间的步长
6.	dtype 输出ndarray的数据类型
'''
print '==========linspace函数============'
x = np.linspace(10, 20, 5)
print x
x = np.linspace(100, 200, endpoint=False)
print x

x = np.linspace(10, 20, 5, endpoint=False,retstep=True)
print x
print '==========linspace函数============'

'''
此函数返回一个ndarray对象，其中包含在对数刻度上均匀分布的数字。 刻度的开始和结束端点是某个底数的幂，通常为 10。

numpy.logscale(start, stop, num, endpoint, base, dtype)
序号	参数及描述
1.	start 起始值是base ** start
2.	stop 终止值是base ** stop
3.	num 范围内的数值数量，默认为50
4.	endpoint 如果为true，终止值包含在输出数组当中
5.	base 对数空间的底数，默认为10
6.	dtype 输出数组的数据类型，如果没有提供，则取决于其它参数
'''

a = np.logspace(1.0,  2.0, num=5)
print a

a = np.logspace(1, 10, num=10,  base=2)
print a