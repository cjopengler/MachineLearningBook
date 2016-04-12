# coding:utf-8

import LR
import numpy as np

def loadDataSet():
    dataMat = []
    labelMat = []

    fr = open('testSet.txt')

    for line in fr.readlines():
        lineArr = line.strip().split()

        # 数据集增加偏置项
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])

        # 标签项
        labelMat.append(int(lineArr[2]))

    return dataMat, labelMat


def plotBestFit(wei):
    '''
    绘制逻辑回归的分界线
    :param wei: 权重
    :return:
    '''

    import matplotlib.pyplot as plt

    weights = wei.getA()


    dataMat, labelMat = loadDataSet()

    dataArr = np.array(dataMat)
    n = np.shape(dataArr)[0]

    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []

    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i, 1])
            ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i, 1])
            ycord2.append(dataArr[i, 2])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='p')
    ax.scatter(xcord2, ycord2, s=30, c='green')

    x = np.arange(-3.0, 3.0, 0.1)
    # 下面的计算是 θ0 + θ1x1 + θ2x2 = 0是边界
    # 所以 x2 = (θ0 + θ1x1)/θ2

    y = (-weights[0] - weights[1]*x)/weights[2]

    ax.plot(x, y)
    plt.xlabel('X1'); plt.ylabel('X2')
    plt.show()


def test():
    print '测试开始...'

    dataArr, labelMat = loadDataSet()

    print dataArr
    print dataArr

    Theta = LR.gradDescent(dataArr, labelMat)
    Theta = LR.stocGradDescent(np.array(dataArr), labelMat)
    Theta = LR.stocGradDescent1(np.array(dataArr), labelMat)

    print 'Theat 类型:', type(Theta)
    print 'Theta计算结果:\n', Theta

    print '绘制分类图像'

    print 'Theta.getA', Theta.A, type(Theta.A), np.shape(Theta.A)

    s = np.array([[1, 2, 3]])

    print 's', s, type(s), np.shape(s)

    # plotBestFit(Theta)
    print '测试结束...'

if __name__ == '__main__':
    test()