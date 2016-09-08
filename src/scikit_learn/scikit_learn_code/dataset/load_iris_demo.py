# coding:utf-8

'''
iris:鸢尾花
鸢尾花数据集是非常容易的多分类的数据集

3个分类,每个分类50个样本,4个维度
该数据集包含了5个属性：
& Sepal.Length（花萼长度），单位是cm;
& Sepal.Width（花萼宽度），单位是cm;
& Petal.Length（花瓣长度），单位是cm;
& Petal.Width（花瓣宽度），单位是cm;
& 种类：Iris Setosa（山鸢尾）、
Iris Versicolour（杂色鸢尾），
以及Iris Virginica（维吉尼亚鸢尾）。

Bunch是字典的子类,事实上就是一个字典
'''

from sklearn.datasets import load_iris
data = load_iris()

print type(data)
print data.keys()
print type(data['target_names'])
print data['target_names']
print type(data['data'])
print data['data'], data['data'].shape
print data['target']
print data['DESCR']
print data['feature_names']
print type(data['feature_names'])
