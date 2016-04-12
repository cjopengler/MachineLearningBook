# coding:utf-8

import LR
import numpy as np

def colicTest():
    frTrain = open('horseColicTest.txt')
    frTest = open('horseColicTest.txt')

    trainingSet = []; trainingLabels = []

    print 'trainingSet: ', type(trainingSet)

    for line in frTrain.readlines():
        currLine = line.strip().split('\t')
        lineArr = []

        for i in range(21):
            lineArr.append(float(currLine[i]))

        trainingSet.append(lineArr)
        trainingLabels.append(float(currLine[21]))

    trainWeights = LR.stocGradDescent1(np.array(trainingSet), trainingLabels, 800)
    print trainWeights

    errorCount = 0; numTestVec = 0.0

    for line in frTest.readlines():
        numTestVec += 1.0

        currLine = line.strip().split('\t')
        lineArr = []

        for i in range(21):
            lineArr.append(float(currLine[i]))

        if int(LR.classifyVector(np.array(lineArr), trainWeights)) != int(currLine[21]):
            errorCount += 1

    errorRate = (float(errorCount) / numTestVec)

    print '错误率: %f' % errorRate

    return errorRate

def multiTest():
    numTests = 10; errorSum = 0.0

    for k in range(numTests):
        errorSum += colicTest()

    print '在 %d 迭代之后的平均错误率是 %f' % (numTests, errorSum / float(numTests))
if __name__ == '__main__':
    multiTest()
