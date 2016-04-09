# coding:utf-8

from tool import docTool
import bayes
import numpy as np

def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1 is abusive, 0 not
    return postingList,classVec

def main():
    print '开始测试...'

    listOPosts, listClasses = loadDataSet()

    myVocabList = docTool.createVocabList(listOPosts)

    print '词汇表:\n', myVocabList

    wordsVec = docTool.setOfWords2Vec(myVocabList, listOPosts[0])

    print '将第一句话转换成向量,存在的单词为1,不存在的单词为0\n', wordsVec

    trainMat = []

    for postinDoc in listOPosts:
        trainMat.append(docTool.setOfWords2Vec(myVocabList, postinDoc))

    p0V, p1V, pAb = bayes.trainNB0(trainMat, listClasses)

    testEntry = ['love', 'my', 'dalmation']

    # 将testEntry转化成特征量的组合,也就是一个要求的样本
    thisDoc = np.array(docTool.setOfWords2Vec(myVocabList, testEntry))

    label = bayes.classifyNB(thisDoc, p0V, p1V, pAb)

    print testEntry, '分类是:',label

    testEntry = ['stupid', 'garbage']

    # 将testEntry转化成特征量的组合,也就是一个要求的样本
    thisDoc = np.array(docTool.setOfWords2Vec(myVocabList, testEntry))

    label = bayes.classifyNB(thisDoc, p0V, p1V, pAb)

    print testEntry, '分类是:',label
    print '测试结束...'

if __name__ == '__main__':
    main()