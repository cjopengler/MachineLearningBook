# coding:utf-8

# 对隐形眼镜的分类

import decisionTree
import plotDecisionTree
import trees

fr = open('lenses.txt')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
fr.close()

print type(lenses)
for i in range(len(lenses)):
    print lenses[i]

print '... end lenses'


lensesFeatName = ['age', 'prescript', 'astigmatic', 'tearRate', 'lenses type']


lensesTree = decisionTree.createTree(lenses, lensesFeatName)
print lensesTree



plotDecisionTree.createPlot(lensesTree)