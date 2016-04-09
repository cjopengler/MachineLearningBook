# coding:utf-8

import decisionTree
import plotDecisionTree

def createDataSet():
    '''创建小量的测试集'''
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    title = ['no surfacing', 'flippers', 'fish']

    return dataSet, title

def demo():
    print '... demo'
    myDat, featNames = createDataSet()
    print myDat

    shannonEnt = decisionTree.calcShannonEnt(myDat)
    print '当前数据集的熵是: ', shannonEnt

    print '... 测试拆分数据集'
    print decisionTree.splitDataSet(myDat, 0, 1)

    print '... 测试最佳特征选择'
    bestFeature = decisionTree.chooseBestFeatureToSplit(myDat)
    print '最好的分类特征是 %s' % bestFeature

    print '... 测试决策树的生成'
    myTree = decisionTree.createTree(myDat, featNames)
    print '生成的决策树是: \n', myTree

    print '... 测试SortedCount'
    classList = ['a', 'b', 'b', 'c', 'e']
    print decisionTree.majorityCnt(classList)

    # print '... 测试绘制树节点'
    # plotDecisionTree.createPlot()

    print '... 测试绘制决策树'
    myTree = plotDecisionTree.retrieveTree(0)
    leafNums = decisionTree.getNumLeafs(myTree)
    treeDepth = decisionTree.getTreeDepth(myTree)
    print myTree
    print '叶子数量:%d, 树高度:%d' % (leafNums, treeDepth)

    # plotDecisionTree.createPlot(myTree)
    print '... 预测'
    featNames = ['no surfacing', 'flippers', 'fish']
    print decisionTree.classify(myTree, featNames, [1, 1])

    print '... 测试和读取决策树存储'
    decisionTree.storeTree(myTree, 'classfierStorage.txt')

    print decisionTree.grabTree('classfierStorage.txt')

    print '... 测试中文情况的决策树读取和存储'
    cnTree = plotDecisionTree.retrieveTree(2)
    print '存储前的决策树: \n', cnTree

    # 对于中文来说,正常的print只能打印出utf-8编码格式
    # 但是可以递归的打印字典 就可以输出中文
    decisionTree.storeTree(cnTree, 'cnTree.txt')
    print decisionTree.grabTree('cnTree.txt')




if __name__ == '__main__':
    demo()