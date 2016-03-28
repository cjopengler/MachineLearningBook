# coding:utf-8

import numpy as np

a = np.arange(0, 60, 10)

print a, a.shape



# 这个小技巧, -1就是6是一个意思.
a = a.reshape(-1, 1)
print a, a.shape

# 这种方式创建出来的表示的是1维,所以b.shape=(5,)
# 这仅仅表示的是1维,不是2维
# 转换成2维, b.shape=(5,1)
b = np.arange(0, 5)
print b, b.shape

# a.shape = (6,1), b.shape=(5,)=(1,5)

print '计算c...'
c = a + b
print c, c.shape

b.shape = (1,5)
b = b.repeat(6, axis=0)

print b, b.shape

a = a.repeat(5, axis=1)
print a, a.shape

# ogrid产生可以广播的行列数组

x,y = np.ogrid[0:5, 0:5]
print x
print y

x, y = np.ogrid[0:1:4j, 0:1:3j]
print x, x.shape
print y, y.shape





