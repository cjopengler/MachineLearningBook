# coding:utf-8

import numpy as np

def img2vector(filename):
    '''将图片文件转换成向量 1*1024的矩阵'''
    returnVect = np.zeros((1, 1024))
    fr = open(filename)

    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            pix = int(lineStr[j])
            returnVect[0,32*i+j] = pix

    return returnVect