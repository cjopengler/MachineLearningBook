# coding:utf-8

import numpy as np

# 使用装饰的函数方式是不是更加帅气呢?

def ufuncDec(a):
    def wraper(func):
        return np.frompyfunc(func(x, 0.6, 0.4, 1.0), 1, 1)
    return wraper

@ufuncDec('a')
def triangle_wave1(x, c, c0, hc):
    x = x - int(x) # 三角波的周期为1，因此只取x坐标的小数部分进行计算
    if x >= c: r = 0.0
    elif x < c0: r = x / c0 * hc
    else: r = (c-x) / (c-c0) * hc
    return r

xx = np.linspace(0, 2, 1000)
yy2 = triangle_wave1(xx)
print yy2