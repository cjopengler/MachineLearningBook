# coding:utf-8

'''
垃圾邮件分类
'''

from tool import docTool
import numpy as np
import bayes

def textParse(bigString):
    '''
    对邮件内容拆分成列表
    :param bigString: 邮件内容
    :return: 列表
    '''
    import re
    listOfTokens = re.split(r'\W*', bigString)

    return [tok.lower() for tok in listOfTokens if len(tok)>2]

def spamTest():
    docList = []
    classList = []
    fullText = []

    for i in range(1, 26):
        wordList = textParse(open('email/spam/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)

        wordList = textParse(open('email/ham/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)

    vocabList = docTool.createVocabList(docList)

    trainingSet = range(50)
    testSet = []

    for i in range(10):
        randIndex = int(np.random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])

    trainMat = []
    trainClasses = []

    for docIndex in trainingSet:
        trainMat.append(docTool.setOfWords2Vec(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])

    p0V, p1V, pSpam = bayes.trainNB0(trainMat, trainClasses)

    errorCount = 0

    for docIndex in testSet:
        wordVector = docTool.setOfWords2Vec(vocabList, docList[docIndex])

        if bayes.classifyNB(wordVector, p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1


    print '错误率: ', float(errorCount) / len(testSet)

if __name__ == '__main__':
    spamTest()