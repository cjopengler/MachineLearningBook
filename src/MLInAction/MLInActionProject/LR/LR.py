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

    return 1/(1+exp(-x))

def gradDescent(dataMatIn, classLabels):
    # 转换成矩阵
    dataMatrix = mat(dataMatIn)
    labelMat = mat(classLabels).transpose()

    m,n = shape(dataMatrix)

    alpha = 0.001
    maxCycles = 500

    weights = ones((n, 1))

    print '1 weights type: ', type(weights), '\n', weights

    for k in range(maxCycles):
        h = sigmoid(dataMatrix * weights)

        error = h - labelMat

        weights = weights - alpha * dataMatrix.transpose()*error
        # 注意 这里的梯度计算没有除以 m, 这是和NG不同的地方.但是因为m是常数,所以不影响计算,但是最好还是除以.
        # 因为公式是这样推导的

    # 在机器学习实践中给的是梯度上升
    # error1 = labelMat - h
    # weights = weights + alpha * dataMatrix.transpose()*error
    # 因为 error = -error1 所以weights的计算结果是完全等价的.

    print '2 weights type: ', type(weights), '\n', weights
    return weights

def stocGradDescent(dataMatrix, classLabels):
    '''
    随机梯度下降 每次只处理一个样本的梯度下降
    :param dataMatrix:
    :param classLabels:
    :return:
    '''

    m,n = shape(dataMatrix)

    alpha = 0.01
    weights = ones(n)

    print 'weights type: ', type(weights), '\n', weights

    for i in range(m):
        h = sigmoid(sum(dataMatrix[i] * weights))
        error = h - classLabels[i]
        weights = weights - alpha * error * dataMatrix[i]

    return mat(weights).T

def stocGradDescent1(dataMatrix, classLabels, numIter=150):
    '''
    随机梯度下降 每次只处理一个样本的梯度下降
    :param dataMatrix:
    :param classLabels:
    :return:
    '''

    m,n = shape(dataMatrix)

    alpha = 0.01
    weights = ones(n)

    for j in range(numIter):
        dataIndex = range(m)

        for i in range(m):
            alpha = 4/(1.0 + j +i) + 0.01

            # 每次去随机数据进行训练
            randIndex = int(random.uniform(0, len(dataIndex)))

            h = sigmoid(sum(dataMatrix[randIndex] * weights))

            error = h - classLabels[randIndex]
            row = dataMatrix[randIndex]
            weights = weights - alpha * error * row

            del randIndex

    # return mat(weights).T
    return weights

def classifyVector(inX, weights):
    prob = sigmoid(sum(inX * weights))

    if prob > 0.5:
        return 1
    else:
        return 0

