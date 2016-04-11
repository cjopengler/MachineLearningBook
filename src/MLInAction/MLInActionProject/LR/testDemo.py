# coding:utf-8

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


def test():
    print '测试开始...'

    dataArr, labelMat = loadDataSet()

    print dataArr
    print labelMat

    print '测试结束...'

if __name__ == '__main__':
    test()