# coding:utf-8

import numpy as np
import math

'''
算法描述:
那么，现在给定一个特征组合W，如何预测W的分类呢？试试上就是求max(P(ci|W)),其中i∈[1,k]. 也就是求W发生的情况的，每个分类出现的概率的最大值。那么这个分类就是W所对应的分类。现在计算这个条件概率,使用bayes公式:


P(c|W) = P(c)*P(W|c)/P(W)=P(c)*P(w1w2...wn|c)/P(w1w2...wn)

假设w1,w2,...,wn是相互独立的，那么有:
P(c|W)=P(c)P(w1|c)P(w2|c)...P(wn|c)/P(w1)P(w2)...P(wn)

1 计算P(c):
	P(c) = 分类的数量/数据集的数量
2 计算P(w1)
	P(w1) = w1的总数量/数据集所有特征的数量.
	注意这里所有单词的数量，因为是计算单词出现的概率
    实际计算中,这个步骤,可以舍去,因为最后是比较条件概率的大小,因为所有的条件概率都会除以P(W)
    所以这一步可以不用计算

3 计算P(w1|c)
	表示在c的分类中，w1的概率,所以
	P(w1|c) = w1在c的集合中出现的数量/c中所有的特征出现的数量

4 求max(P(ci|W)),注意因为是求最大,所以P(W)是不需要计算的,因为所有的概率最终都除以这个数据.
所以:max(P(ci|W)) = max(P(c)*P(W|c)),下面的代码中在求概率的时候,也没有计算P(W)

'''

def trainNB0(trainMatrix, trainCategory):
    '''
    计算分类标签的概率,以及每一个特征值的条件概率.

    :param trainMatrix: 矩阵数据
    :param trainCategory: 分类的标签
    :return:
    '''
    # 数据集的总条目数
    numTrainDocs = len(trainMatrix)

    # 分类标签中,也就是c1,标签为1的数量,trainCategory非0就是1 所以计算sum即可
    labelCount = sum(trainCategory)

    #计算P(c1)也就是标签为1的概率
    pAbusive = labelCount / float(numTrainDocs)

    #计算P(w|c0)和P(w|c1)
    numFeaturs = len(trainMatrix[0])

    # featrue为0和的数组,用来存储每个featrue的数量
    # p0Num = np.zeros(numFeaturs)
    # p1Num = np.zeros(numFeaturs)

    # 为什么不使用0作为初始化?因为会出现概率为0的情况,最后计算乘积将为0
    p0Num = np.ones(numFeaturs)
    p1Num = np.ones(numFeaturs)

    # 每个分类下的所有feature的总量
    # p0Denom = 0.0
    # p1Denom = 0.0

    p0Denom = 2.0
    p1Denom = 2.0

    for i in range(numTrainDocs):

        if trainCategory[i] == 1:
            # 分类标签为1的情况下,每个单词的数量列表
            p1Num += trainMatrix[i]
            # 分类标签为1的情况下,所有单词的数量
            p1Denom += sum(trainMatrix[i])

        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])

    # P(w|c1)
    # p1Vect = p1Num / p1Denom
    p1Vect = np.log(p1Num / p1Denom)

    # P(w|c0)
    # p0Vect = p0Num / p0Denom
    p0Vect = np.log(p0Num / p0Denom)

    # 这里为什么使用log,是因为当P1*P2...会得到很小的值,会导致为0
    # 现在每一个特征量取了log,所以 log(P1*P2...)=log(P1)+log(P2)+....
    # 这样变化就不会引起很小的值的问题.但是同时,原先的P1*P2...的乘法计算,修改成加法运算

    return p0Vect, p1Vect, pAbusive


def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    '''
    对vec2Classiy,这样一条记录,也就是特征量的组合进行分类计算
    :param vec2Classify: 记录,由wk个特征量组合
    :param p0Vec: 标签为0时候的每个特征量的条件概率
    :param p1Vec: 标签为1时候的每个特征量的条件概率
    :param pClass1: 标签为1时候的概率
    :return:0或者1的分类标签
    '''
    # 注意,因为所有的概率都取了log,所以原先的条件概率的乘法计算变成了加法计算
    p1 = sum(vec2Classify * p1Vec) + math.log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + math.log(pClass1)

    if p1 > p0:
        return 1
    else:
        return 0