# coding:utf-8

from sklearn.datasets import load_digits
digits = load_digits()
print(digits.data.shape)

image = digits.images[0]


print type(image), image.shape
print image


import pylab as pl
pl.gray()
pl.matshow(image)
pl.show()

