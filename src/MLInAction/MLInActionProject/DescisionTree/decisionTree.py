# coding:utf-8

import math
import operator


def calcShannonEnt(dataSet):
    '''计算指定数据的熵
        数据结构和算法:
        dataSet的最后一列是label.
        熵是计算所有label的概率p与log(p)的乘积的和
    '''

    # 计算数据集的行数, 注意这里的dataSet类型是list不是numpy.array
    numEntries = len(dataSet)

    print 'numEntries %d' % (numEntries)

    # 字典用来存放label以及数量
    labelCounts = {}

    # 逐行获取进行计算
    for featVec in dataSet:
        # 最后一列是label
        currentLabel = featVec[-1]

        print 'currentLabel: %s' % currentLabel

        # 字典中是否保存了当前label的值, 计算当前label的数量
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0

        labelCounts[currentLabel] += 1

    shannonEnt = 0.0

    # 计算每一个label的概率,并且相加
    for key in labelCounts:
        count = labelCounts[key]
        print 'key:',key,' count: ',count
        prob = float(count) / numEntries
        shannonEnt -= prob * math.log(prob, 2)

    return shannonEnt

def splitDataSet(dataSet, axis, value):
    '''
        根据特定值和特定轴(列)进行数据集拆分,也就是对某个特征量的所有值进行划分.
        举例子来说,例如第2个特征值有1,2,3,4 四个数值,那么splitDataSet就是将
        数据集分成, value=1,value=2,value=3,value=4的4个子数据集.

        数据结构:
        axis表示的是列;value表示的是特定的特征量的值

        算法:
        在axis列中找到等于value的行i.
        将i行的[0, axis)和[axis+1, end),也就是排除axis列,组成新的一行

        对dataSet中每一行执行上面的操作也就是,i从0执行到dataSet的最后一行
    '''
    retDataSet = []

    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)

    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    '''
        选择最好的数据集,也就是选择那个熵最小的数据集

        算法:
        这里显然是一个双层循环.因为要遍历所有feature,
        再遍历每个feature中的值(value),
        用每个feature中的每个值(value)进行数据集拆分,
        得到该feature.value下的子数据集.
        可见一共会有, feature1.value数量 + feature2.value +...+featuren.value个子数据集

        熵的计算:
        计算feature的熵,也就是计算所有子数据集的熵的和,选择最小的那一个,作为划分的方式.因为熵越小,表示信息包含的越少,也就是越集中.
    '''

    # 特征值的数量,要讲最后的label减去
    numFeatures = len(dataSet[0]) - 1

    # 计算最初的熵
    baseEntropy = calcShannonEnt(dataSet)

    bestInfoGain = 0.0
    bestFeature = -1

    # 循环所有的feature
    for i in range(numFeatures):
        # 获取每个feature中的所有值, 下面的代码效率不高,事实上我们就是获取第i列的数据
        # 但是因为dataSet是列表,不是numpy的array,所以获取起来不方便
        featList = [example[i] for example in dataSet]

        # 因为在所有行中feature的特征值可能重复,所以需要去重
        uniqueVals = set(featList)

        # 当前feature的熵,也就是每一个value下的熵的和
        newEntropy = 0.0

        # 循环遍历每个feature的value
        for value in uniqueVals:
            # 拆分成子数据集
            subDataSet = splitDataSet(dataSet, i, value)

            # 计算子数据集的熵
            # 计算子集占整个数据集的百分比
            prob = len(subDataSet) / float(len(dataSet))
            # 计算当前feature总的熵
            newEntropy += prob * calcShannonEnt(subDataSet)

        # 除去当前子集的其他数据集的熵越大,说明当前子集的熵越小
        infoGain = baseEntropy - newEntropy

        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i

    return bestFeature

def majorityCnt(classList):
    '''
    从label列表中选择出现次数最多的label作为最终的label
    :param classList: label列表
    :return: 出现次数最多的label
    '''
    classCount = {}
    for vote in classList:
        if vote not in classCount:
            classCount[vote] = 0
        classCount[vote] += 1

    # sorted排序后将字典变成了一个列表,每一个元素是一个二元组,
    # 二元组第一个元素是key;第二个元素是count
    sortedClassCount = sorted(classCount.iteritems(),
                              key = operator.itemgetter(1),
                              reverse=True)

    return sortedClassCount[0][0]

def createTree(dataSet, featureNames):
    '''
    递归创建决策树.

    算法:
    递归创建决策树.递归的出口,包含该两个:
        1. 在该节点中,所有的label都是一样的,也就是分类是一样的,
        2. 所有的feature都已经划分完毕,但是也有可能包含的label是不一样的,那么使用最多的作为最终分类

    数据结构:
    使用字典进行存储树状结构, feature名字作为根,所有子数据集作为儿子节点

    :param dataSet: 数据集,要注意这里的数据集的最后一列是label
    :param featureNames: 数据的feature名称
    :return: 树形结构 {'title1':{title1.value1:'no',
                                title1.Value2:{
                                                title2:{title2.value1:'no',
                                                        title2.value2:'yes'
                                                       }
                                              }
                               }
                     }
    '''

    # 取出标签列
    classList = [example[-1] for example in dataSet]

    # 所有的标签都是同一个类别,返回这个标签值
    if classList.count(classList[0]) == len(classList):
        return classList[0]

    # 所有的feature都被分类完毕,只剩下label, 从中选择出现次数最多的作为分类标准
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)

    # 选择分类feature
    bestFeat = chooseBestFeatureToSplit(dataSet)

    # 提取bestFeature的名字
    bestFeatName = featureNames[bestFeat]

    # 建立树的字典结构
    myTree = {bestFeatName:{}}

    del(featureNames[bestFeat])

    # 取出当前分类的featrue的所有制
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)

    # 循环所有featrue.value建立儿子
    for value in uniqueVals:
        subFeatureNames = featureNames[:]

        #根据每一个value拆分出子数据集
        subDataSet = splitDataSet(dataSet, bestFeat, value)

        #递归创建儿子
        myTree[bestFeatName][value] = createTree(subDataSet, subFeatureNames)

    return myTree

def getNumLeafs(myTree):
    '''
    获取决策树的叶子节点的数目

    数据结构:
    决策树是一个字典结构,父亲节点是'key',儿子又是一个字典,
    当儿子字典的value不是一个字典的时候,就是叶子节点.

    算法:
    递归计算叶子节点的数目

    :param myTree: 决策树的字典对象
    :return: 叶子的数量
    '''
    numLeafs = 0

    # 获取根节点
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]

    # 遍历所有的儿子节点
    for key in secondDict.keys():
        # 儿子是个字典,那就不是叶子节点,需要递归处理
        if type(secondDict[key]).__name__ == 'dict':
            numLeafs += getNumLeafs(secondDict[key])
        else:
            # 叶子节点就直接 +1
            numLeafs += 1

    return numLeafs

def getTreeDepth(myTree):
    '''
    计算树的高度

    算法:
    树的高度是max(所有子树)+1

    :param myTree: 决策树字典结构
    :return: 树的高度
    '''

    maxDepth = 0

    # 获取根节点
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]

    # 循环所有子树
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:
            # 叶子节点直接返回1
            thisDepth = 1

        # 所有子树中选择最高的
        if thisDepth > maxDepth:
            maxDepth = thisDepth

    return maxDepth

def classify(inputTree, featNames, testVec):
    '''
    对指定的输入数据的分类

    算法:
    对树进行递归查找,直到找到叶子节点

    :param inputTree: 训练好的决策树
    :param featNames:
    :param testVec:
    :return:
    '''

    # 根节点
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]

    # 找到当前跟节点的特征索引
    featIndex = featNames.index(firstStr)

    # 寻找当前树的根节点与testVec匹配的点
    for key in secondDict.keys():

        if testVec[featIndex] == key:
            # 匹配上了 递归下降到子树
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featNames, testVec)

            else:
                # 非子树,返回分类标签
                classLabel = secondDict[key]

    return classLabel

def storeTree(inputTree, fileName):
    '''
    存储决策树的字典到文件中
    :param inputTree: 决策树
    :param fileName: 文件名
    :return: Noe
    '''
    import pickle
    fw = open(fileName, 'w')
    pickle.dump(inputTree, fw)
    fw.close()

def grabTree(fileName):
    '''
    从文件中获取决策树
    :param fileName:决策树的文件名
    :return: 字典结构的决策树
    '''
    import pickle
    fr = open(fileName)
    return pickle.load(fr)