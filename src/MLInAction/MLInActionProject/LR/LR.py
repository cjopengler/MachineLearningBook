# coding:utf-8

from numpy import *

'''
逻辑回归
'''

def sigmoid(x):
    '''
    sigmoid函数实现
    :param x: 矩阵或者任意实数
    :return: sigmoid函数值
    '''

    return 1/(1+exp(x))