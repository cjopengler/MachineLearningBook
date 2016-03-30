# coding:utf-8

import decisionTree

def createDataSet():
    '''创建小量的测试集'''
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    title = ['no srurfacting', 'flippers', 'fish']

    return dataSet, title

def demo():
    print '... demo'
    myDat, title = createDataSet()
    print myDat

    shannonEnt = decisionTree.calcShannonEnt(myDat)

    print '当前数据集的熵是: ', shannonEnt


if __name__ == '__main__':
    demo()