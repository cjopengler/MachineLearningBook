# coding:utf-8

import knn
import numpy as np

def train():
    '''对knn进行训练'''

    datingDataMat, datingLables = knn.file2matrix('datingTestSet2.txt')

    normMat, rangeVals, minVals = knn.autoNorm(datingDataMat)

    print normMat
    print datingLables

    # knn.plotData(datingDataMat, datingLables)



    # 用作交叉验证集的数量百分比
    hoRatio = 0.10
    # 数据集的总数量
    m = normMat.shape[0]

    # 测试集
    numTestVecs = int(m*hoRatio)

    errorCount = 0.0

    for i in range(numTestVecs):
        classifierResult = knn.classify0(normMat[i, :],
                                         normMat[numTestVecs:m, :],
                                         datingLables[numTestVecs:m],
                                         3)

        print '分类器返回: %d, 实际的结果是:%d' % (classifierResult, datingLables[i])

        if classifierResult != datingLables[i]:
            errorCount += 1.0


    print '错误率是: %f' % (errorCount / (float(numTestVecs)))

def predict():
    resultList = ['一点也不喜欢', '有点喜欢', '非常喜欢']
    percentTats = float(raw_input('玩游戏的时间是: '))
    ffMiles = float(raw_input('每年的飞行公里数: '))
    iceCream = float(raw_input('每年消耗的冰淇淋: '))

    datingDataMat, datingLabels = knn.file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = knn.autoNorm(datingDataMat)

    inArr = np.array([ffMiles, percentTats, iceCream])

    # 对输入数据的正规化处理
    inArrNorm = (inArr - minVals) / ranges

    classifierResult = knn.classify0(inArrNorm, normMat, datingLabels, 3)

    print '预测你可能喜欢这个人的程度:', resultList[classifierResult-1]