# coding:utf-8

# ndarray类是用来表示多维矩阵的类
# ufunc是对ndarray进行运算的函数
# 目标: 对比Octave/Matlab与python的实现

import numpy
from numpy import array, arange

a = array([1, 2, 3, 4])
print a

b = array((5, 6, 7, 8))
print b

# 二维数组
c = array([[1, 2, 3, 4], [5, 6, 7, 9], [9, 10, 11, 12]])
print c

d = array([[1, 2], [5, 6], [7, 8]])
print d, d.dtype

## 与Octave的对比

# 数组的大小,对应Octave:size
print c.shape, a.shape

# 疑问 a.shape返回(4,)是表示4行1列?

# 改变shape,也就是改变了数组的组成形式
c.shape = (4, 3)
print c

print a
a.shape = (1,4)
print 'a:',a

# 通过改变shape的方式,可以知道,任何一个矩阵本质上是线性存储的,
# 然后再通过shape展现的方式来以不同的方式展现, 这个函数类似 Octave:reshape

# 所以我们创建矩阵,可以先创建m*n的一维矩阵,然后再分维度
# 除了使用列表进行创建矩阵之前,还可以使用其他的方式来创建矩阵

# 注意这是一个开区间, [0, 0.1) 这个地方与Octave不同 Octave是[0, 0.1]
# 使用步长来创建
print arange(0, 1, 0.1)

# 指定区间和个数,依照等差数列来创建,默认是闭区间,可以设置endpoint=flase来表示开区间
print numpy.linspace(0, 1, 12)
print numpy.linspace(0, 1, 12, endpoint=False)

# 以等比数列创建, 其中start表示的是10的次数,所以下面是表示1到100
print numpy.logspace(0, 2, 20)

# 使用函数创建矩阵,函数的参数是矩阵的下标(i,j)
# 创建一维矩阵

def func(i):
    return i%4 + 1

print numpy.fromfunction(func, (10,))

# 创建m*n矩阵, i表示行号;j表示列号
def func(i, j):
    return (i+1)*(j+1)

print numpy.fromfunction(func, (9, 9))

# 存取元素
a = numpy.arange(10)
print a
print a[5]
print a[3:5]
print a[:5]
print a[:-1]
a[2:4] = (100, 101)
print a
print a[:]

# 使用整数进行存取
x = numpy.arange(10, 1, -1)
print x

# 这时候因为x是矩阵类型,所以可以使用整数列表作为下标,来获取x的序列
print x[[3, 3, 1, 8]]

b = x[numpy.array([3, 3, -3, 8])]
print b

# 也可而已使用布尔数组来获取x中的元素,这一点在Octave中也是包含的
x = numpy.arange(5, 0, -1)
print x[[True, False, True, False, False]]

# 多维数组数组的存取使用的是元组(i,j),但是因为元组使用的时候可以将括号去掉所以这样的存取就会使得与Octave基本一致

a = numpy.linspace(1, 25, 5*5, dtype=numpy.int64)
a.shape = (5, 5)

print a, a.dtype

# 注意呀下标是从0开始的,这是与Octave的区别,下面的用法与Octave是一样的
print a[0, 3:5]
print a[3:, 3:]
print a[:, 2]

# 使用布尔值来存取
mask = numpy.array([1, 0, 1, 0, 0], dtype=numpy.bool)

print a[mask, 2]




