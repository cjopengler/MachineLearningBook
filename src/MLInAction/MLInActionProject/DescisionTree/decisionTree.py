# coding:utf-8

import math


def calcShannonEnt(dataSet):
    '''计算指定数据的熵
        数据结构和算法:
        dataSet的最后一列是label.
        熵是计算所有label的概率p与log(p)的乘积的和
    '''

    # 计算数据集的行数, 注意这里的dataSet类型是list不是numpy.array
    numEntries = len(dataSet)

    print 'numEntries %d' % (numEntries)

    # 字典用来存放label以及数量
    labelCounts = {}

    # 逐行获取进行计算
    for featVec in dataSet:
        # 最后一列是label
        currentLabel = featVec[-1]

        print 'currentLabel: %s' % currentLabel

        # 字典中是否保存了当前label的值, 计算当前label的数量
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0

        labelCounts[currentLabel] += 1

    shannonEnt = 0.0

    # 计算每一个label的概率,并且相加
    for key in labelCounts:
        count = labelCounts[key]
        print 'key:',key,' count: ',count
        prob = float(count) / numEntries
        shannonEnt -= prob * math.log(prob, 2)

    return shannonEnt

def splitDataSet(dataSet, axis, value):
    '''
        根据特定值和特定轴(列)进行数据集拆分

        数据结构:
        axis表示的是列;value表示的是特定的特征量的值

        算法:
        在axis列中找到等于value的行i.
        将i行的[0, axis)和[axis+1, end),也就是排除axis列,组成新的一行

        对dataSet中每一行执行上面的操作也就是,i从0执行到dataSet的最后一行
    '''