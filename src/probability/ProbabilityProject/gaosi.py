# coding:utf-8

'''
标准高斯分布函数图像绘制

'''

import matplotlib.pyplot as plt
import numpy as np

def gaosi():
    gaosiNData = open('gaosiNData.txt', 'rU')

    # x表示随机变量, fx表示概率密度, phi表示概率分布函数
    x = []; fx = []; phi = [];

    i = 0
    for line in gaosiNData:
        lineArr = line.split('\t')
        x.append(float(lineArr[0]))
        fx.append(float(lineArr[1]))
        phi.append(float(lineArr[2]))

    gaosiNData.close()

    return x, fx, phi

def sigmoid(x):

    return 1/(1+np.exp(-x))


def main():
    x, fx, phi = gaosi()

    print x
    print fx
    print phi

    plt.plot(x, phi)

    plt.plot([-4,4],[0.33,0.33])
    plt.plot([-4,4],[0.66,0.66])

    # simod
    xArray = np.array(x)
    # xArray = np.array([1, 2, 3])
    aArray = np.array(x)
    print type(xArray)
    # print xArray
    # print aArray


    sigmoidValue = sigmoid(xArray)

    error = sum((np.array(phi) - sigmoidValue)**2)/len(sigmoidValue)

    print error

    plt.plot(xArray, sigmoidValue)
    plt.show()



if __name__ == '__main__':
    main()


