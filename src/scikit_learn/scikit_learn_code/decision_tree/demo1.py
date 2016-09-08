# coding:utf-8

from sklearn import tree

X = [[0, 0], [1, 1], [2,3], [4, 8]]
Y = [0, 1, 0, 1]
clf = tree.DecisionTreeClassifier()
clf.fit(X, Y)

test = [[2, 2], [1, 1.5], [0, 0]]
print clf.predict(test)
print clf.predict_proba(test)

