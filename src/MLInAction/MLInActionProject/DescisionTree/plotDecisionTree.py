# coding:utf-8

import matplotlib.pyplot as plt
import decisionTree

decisionNode = dict(boxstyle='sawtooth', fc='0.8')
leafNode = dict(boxstyle='round4', fc='0.8')
arrow_arg = dict(arrowstyle='<-')

def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    '''
    绘制树形节点
    :param nodeTxt: 节点的文本内容
    :param centerPt: 文本的中心坐标
    :param parentPt: 箭头的起始坐标
    :param nodeType: 节点类型
    :return: None
    '''
    createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction',
                            xytext=centerPt, textcoords='axes fraction',
                            va='center', ha='center', bbox = nodeType,
                            arrowprops = arrow_arg)


def retrieveTree(i):
    '''
    预先定义的i+1棵树,为了测试用
    :param i: 第i棵树
    :return: 决策树字典结构
    '''
    listOfTrees =[{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
                  {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}},
                  {u'无法浮出水面': {0: 'no', 1: {u'有脚蹼': {0: 'no', 1: 'yes'}}}}]
    return listOfTrees[i]

def plotMidText(cntrPt, partenPt, txtString):
    '''
    在父子之间的连线上标记文字
    :param cntrPt: 当前儿子节点坐标
    :param partenPt: 当前父亲节点坐标
    :param txtString: 标记文字
    :return: None
    '''
    xMid = (partenPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (partenPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString)


def plotTree(myTree, parentPt, nodeTxt):
    '''
    算法: 递归绘制.先绘制父亲节点,然后再绘制所有儿子节点
    :param myTree: 决策树
    :param parentPt: 父亲节点坐标
    :param nodeTxt: 当前节点的文本
    :return: None
    '''
    numLeafs = decisionTree.getNumLeafs(myTree)
    depth = decisionTree.getTreeDepth(myTree)

    # 获取根节点 文字描述
    firstStr = myTree.keys()[0]

    # 寻找中心点, 一半叶子节点的位置
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs))/2.0/plotTree.totalW, plotTree.yOff)

    # 绘制父亲到当前点的连线标注
    plotMidText(cntrPt, parentPt, nodeTxt)

    # 绘制当前节点的文字描述,到这里跟节点的相关信息绘制完毕
    plotNode(firstStr, cntrPt, parentPt, decisionNode)

    # 绘制儿子节点
    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD

    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            # 绘制子树
            plotTree(secondDict[key], cntrPt, str(key))
        else:
            # 绘制叶子
            plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
            plotNode(secondDict[key],
                     (plotTree.xOff, plotTree.yOff),
                     cntrPt,
                     leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff),
                        cntrPt,
                        str(key))

    plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD



def createPlot(inTree):
    '''
    绘制决策树
    :param inTree: 决策树
    :return: Noe
    '''
    fig = plt.figure(1, facecolor='white')
    fig.clf()

    axprops = dict(xticks=[], yticks=[])
    createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)
    plotTree.totalW = float(decisionTree.getNumLeafs(inTree))
    plotTree.totalD = float(decisionTree.getTreeDepth(inTree))

    plotTree.xOff = -0.5/plotTree.totalW
    plotTree.yOff = 1.0
    plotTree(inTree, (0.5, 1.0), '')
    plt.show()


def createPlotTest():
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    createPlot.ax1 = plt.subplot(111, frameon=False)
    plotNode(u'决策节点', (0.5, 0.1), (0.1, 0.5), decisionNode)
    plotNode(u'叶子节点', (0.8, 0.1), (0.3, 0.8), leafNode)
    plt.show()
