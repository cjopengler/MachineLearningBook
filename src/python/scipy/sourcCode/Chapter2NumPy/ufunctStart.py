# coding:utf-8

# ufunc是对数组中的每一个元素进行操作
# 这有点类似于 Octave: a .* 3 这种操作. 以及Octave中所有的函数
# 都可以直接针对矩阵进行操作
# 对于numpy来说,就是可以对np的矩阵对象进行操作

import numpy as np

x = np.linspace(0, 2*np.pi, 10)
y = np.sin(x)

print y

# 下面的函数是将一个普通函数包装成ufunc

def triangle_wave(x, c, c0, hc):
    x = x - int(x) # 三角波的周期为1，因此只取x坐标的小数部分进行计算
    if x >= c: r = 0.0
    elif x < c0: r = x / c0 * hc
    else: r = (c-x) / (c-c0) * hc
    return r

triangel_wave_ufunc = np.frompyfunc(lambda x:triangle_wave(x, 0.6, 0.4, 1.0), 1, 1)
x = np.linspace(0, 2, 1000)
y2 = triangel_wave_ufunc(x)
# print y2

print np.add.reduce([1, 2, 3])

a = np.array([[1,2,3], [4, 5, 6]])
print a
print np.add.reduce(a, axis=0),'\n',np.add.reduce(a, axis=1)

print '... accumulate'
print np.add.accumulate(a), '\n', np.add.accumulate(a, axis=1)

print '... reduceat'
# reduceat 的区间是[start, stop)
# 所以下面
# 1: [0, 1) = a[0]=1; 2:[1,0)=a[1]=2; 3:[0, 2)=a[0]+a[1]=3
# 4: [2, 0]=a[2]=3; 5:a[0, 3]=a[0] + a[1] + a[2] = 6
# 6:[0,:]=a[0]+a[1]+a[2]+a[3]=1+2+3+4 = 10
b = np.array([1, 2, 3, 4])
result = np.add.reduceat(b, indices=[0, 1, 0, 2, 0, 3, 0])
print result

print '... outer'
print np.multiply.outer([1,2,3,4,5], [2, 3, 4])