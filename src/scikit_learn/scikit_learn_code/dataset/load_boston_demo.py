# coding:utf-8
from sklearn.datasets import load_boston
boston = load_boston()
print(boston.data.shape)
print boston.DESCR
print boston.data[:5, :]
