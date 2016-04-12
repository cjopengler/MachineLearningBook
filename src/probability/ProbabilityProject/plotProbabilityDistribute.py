# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt

def probability(timesArray):
    '''
    输入一个次数的array,来计算概率
    :param timesArray:
    :return: 概率的array
    '''
    print 'timesArray', timesArray
    baseArr = np.ones(len(timesArray)) * 5.0/6.0
    print 'baseArr', baseArr

    pArr = np.array(len(timesArray))

    pArr = np.power(baseArr, timesArray) * 1.0/6.0

    return pArr


def plotProbability(times, pArr):
    figure = plt.figure()
    ax = figure.add_subplot(111)
    ax.scatter(times, pArr)

    plt.draw()
    plt.show()

def test():
    print '...'

    times = range(50)

    print type(times)
    pArr = probability(times)
    print pArr


    plotProbability(times, pArr)
    print '...'

if __name__ == '__main__':
    test()