# coding:utf-8

from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.externals.six import StringIO
import pydotplus

iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

#with open('iris.dot', 'w') as f:
    #f = tree.export_graphviz(clf, out_file=f)

from sklearn.externals.six import StringIO
import pydot
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
print type(graph)

graph.write_pdf("iris.pdf")

print clf.predict(iris.data[:100, :])
print clf.predict_proba(iris.data[:, :])
