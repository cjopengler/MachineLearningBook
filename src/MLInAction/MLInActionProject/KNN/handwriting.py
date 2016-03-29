# coding:utf-8

import tool.imageTool as imageTool
import os
import numpy as np
import knn

def train(trainImagePath, testImagePath):
    hwLabels = []
    trainingFileList = os.listdir(trainImagePath)

    m = len(trainingFileList)

    trainningMat = np.zeros((m, 1024))

    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainningMat[i, :] = imageTool.img2vector('%s/%s' % (trainImagePath,fileNameStr))

    testFileList = os.listdir(testImagePath)
    errorCount = 0.0

    mTest = len(testFileList)

    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = imageTool.img2vector('%s/%s' % (testImagePath,fileNameStr))
        classifierResult = knn.classify0(vectorUnderTest, trainningMat, hwLabels, 3)

        print '分类器返回的数字是:%d, 实际的数字是:%d' %(classifierResult, classNumStr)

        if (classifierResult != classNumStr):
            errorCount += 1.

    print '总的错误数: %d' % errorCount
    print '错误率: %f' % (errorCount / float(mTest))

def main():
    print 'main...'
    testVector = imageTool.img2vector('../testDigits/0_13.txt')
    print testVector[0, 0:31]

    train('../trainingDigits', '../testDigits')

if __name__ == '__main__':
    main()