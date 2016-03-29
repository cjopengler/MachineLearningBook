# coding:utf-8

from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt

def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify0(inX, dataSet, labels, k):
    '''
    inX: 预测的数据
    dataSet: 现有的数据集
    labels: 现有的数据集的labels
    k: 相似的数量

    计算步骤:
    1 计算出已知类别数据集中的点与当前点之间的距离
    2 按照距离进行递增排序
    3 选取与当前点距离最小的k个点.
    4 确定前k个点所在类别出现的频率
    5 返回出现频率最高的类别作为预测分类
    '''

    # 返回数据集中的行,m
    dataSetSize = dataSet.shape[0]

    # tile将inX扩展成m行,这样与dataSet的行数是一致的
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet

    # 计算差的平方
    sqDiffMat = diffMat**2

    # 将列进行相加 axis=1表示的是列
    sqDistances = sqDiffMat.sum(axis = 1)

    # 计算距离
    distances = sqDistances**0.5

    # 将距离进行排序
    sortedDistIndices = distances.argsort()

    # 建立字典.key=lable,value=count
    classCount = {}

    # 将距离最小的前k个存放进入字典,并且设置lable的数量
    for i in range(k):
        voteIlabel = labels[sortedDistIndices[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1

    # 对字典进行排序,按照value值的大小,降序排列
    sortedClassCount = sorted(classCount.iteritems(),
                              key=operator.itemgetter(1),
                              reverse=True)

    # 返回第一个字典值
    return sortedClassCount[0][0]

def file2matrix(filename):
    '''将数据文件转换成matrix'''
    fr = open(filename)

    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)

    # 矩阵,因为只有三个元素所以是m*3
    returnMat = zeros((numberOfLines, 3))

    # 这是一个列表,每一个列表的数值是一个label
    classLabelVector = []

    index = 0
    for line in arrayOLines:
        # 先strip
        line = line.strip()
        # 使用\t进行拆分
        listFromLine = line.split('\t')
        # 对矩阵的每一个元素进行赋值
        returnMat[index,:] = listFromLine[0:3]
        # 将label赋值
        classLabelVector.append(int(listFromLine[-1]))
        index += 1

    return returnMat, classLabelVector


def plotData(datingMatrix, classLabelVector):
    '''绘制矩阵数据'''
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(datingMatrix[:,1], datingMatrix[:,2],
               15.0*array(classLabelVector),
               15.0*array(classLabelVector))
    plt.show()


def autoNorm(dataSet):
    '''对数据集进行归一化处理使用的算法是:
        newValue = (oldValue - min)/(max - min)
        其中:max是数据集中最大值;min是足校直
    '''

    print 'dataSet类型: %s, size(%d, %d)' % (type(dataSet), dataSet.shape[0], dataSet.shape[1])

    # 从当前列中选取最小值和最大值
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals

    # 产生一个m*n的0矩阵
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]

    # dataSet:m*n, tile:m*n 进行减法操作,类似A .- B
    normDataSet = dataSet - tile(minVals, (m,1))
    # 除法操作,类似: A ./ B 而非矩阵出发
    # 矩阵出发:linalg.solve(matA, matB)
    normDataSet = normDataSet / tile(ranges, (m,1))

    return normDataSet, ranges, minVals