# coding:utf-8

def createVocabList(dataSet):
    '''
    将字符串数组列表转换成单词表
    :param dataSet: 字符串数组列表
    :return: 单词表的列表
    '''
    vocabSet = set([])

    for document in dataSet:
        vocabSet = vocabSet | set(document)

    return list(vocabSet)

def setOfWords2Vec(vocabList, inputSet):
    '''
    根据输入的一句话来标记词汇表的特征值.
    这是基于词集的,也就是是否出现
    :param vocabList:词汇表
    :param inputSet: 输入的一句话
    :return: 标记向量
    '''
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else: print '%s 不在词汇表中' % word

    return returnVec


def bagSetOfWords2Vec(vocabList, inputSet):
    '''
    根据输入的一句话来标记词汇表的特征值.
    这是基于词包的,也就是每个次出现的次数作为特征值
    :param vocabList:词汇表
    :param inputSet: 输入的一句话
    :return: 标记向量
    '''
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] + 1
        else: print '%s 不在词汇表中' % word

    return returnVec