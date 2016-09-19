# coding:utf-8
"""
年龄分析,年龄是一个很重要的因素,而且年龄的缺失也很多,所以需要建立一个模型来预测是否是儿童
儿童的定义是<16岁
"""

import pandas as pd
from pandas import DataFrame
from pandas import Series
from sklearn.base import BaseEstimator
from sklearn.base import TransformerMixin
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.grid_search import GridSearchCV


class AgeTransformV2(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        age = X[['SibSp', 'Parch','Age']][Series.notnull(X['Age'])]

        age_nan = X[['SibSp', 'Parch']][Series.isnull(X['Age'])]

        y_child = age['Age'].map(lambda age: 1 if age < 16 else 0)
        y_child = y_child.rename('y_child')

        age.drop('Age', axis=1, inplace=True)

        lr = LogisticRegression()
        paramters = {'C':[0.01, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3]}

        self.grid_search = GridSearchCV(lr, paramters, cv=5, n_jobs=-1)

        self.grid_search.fit(age, y_child)

        #print self.grid_search.best_params_
        #print self.grid_search.best_score_


        return self

    def predict_age(self, sp):
        pred_age = self.grid_search.predict(sp)
        return pred_age[0]

    def transform(self, X, y=None):

        pred_age_train = X[['SibSp', 'Parch']][Series.isnull(X['Age'])]

        pred_age = pred_age_train.apply(self.predict_age, axis=1)
        # 相等的赋值会按照 行号来进行赋值的
        X['Age'][Series.notnull(X['Age'])] = X['Age'][Series.notnull(X['Age'])].map(lambda age: 1 if age < 16 else 0)
        X['Age'][np.isnan(X['Age'])] = pred_age

        X.rename(columns={'Age':'Child'}, inplace=True)

        return X


###############################################################################


class SexTransformerV2(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):

        sex_dummies = pd.get_dummies(X['Sex'])
        sex_dummies.columns = ['Female', 'Male']

        # 删除掉'sex'
        X.drop('Sex', axis=1, inplace=True)

        X = pd.concat([X, sex_dummies], axis=1)
        return X


if __name__ == '__main__':
    X_train = pd.read_csv('../input/train.csv')

    y_train = X_train['Survived']

    aatf = AgeTransformV2()
    X_train = aatf.fit_transform(X_train)
    print X_train.head(10)

    sex_tf = SexTransformerV2()
    X_train = sex_tf.fit_transform(X_train)
    print X_train.head(10)

