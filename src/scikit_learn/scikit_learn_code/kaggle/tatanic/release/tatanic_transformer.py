# coding:utf-8

from sklearn.base import TransformerMixin
from sklearn.base import BaseEstimator
import pandas as pd
from pandas import DataFrame
from pandas import Series
import numpy as np

class EmbarkedTransformer(BaseEstimator, TransformerMixin):
    """
    登船城市的数据转换
    """
    def __init__(self):
        pass

    def fit(self, X, y=None):
        """
        fit用来训练X数据集.
        对于Embarked来说,fit这部分没有任何工作要处理,因为没有内部的参数要保存

        :param X:训练的数据集
        :return: 自己,这里一定要return self,不然 在父类TransformerMixin中的fit_transform会调用失败
        """


        return self


    def transform(self, X, y=None):
        """
        用fit中训练好的参数来变换X,比如均值方差之类的用fit函数来训练好,再转换未来的数据
        直接在这里进行数据的转换即可。就是删除S并且,将另外的两个维度进行向量化
        :param X: DataFrame数据
        :return:
        """
        embarked_tatanic_dummies = pd.get_dummies(X['Embarked'])
        embarked_tatanic_dummies.drop('S', axis=1, inplace=True)

        X = pd.concat([X, embarked_tatanic_dummies],
                                     axis=1)
        X.drop('Embarked', axis=1, inplace=True)

        return X

###############################################################################

class FareTransformer(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X['Fare'].fillna(X['Fare'].mean(), inplace=True)
        X['Fare'] = X['Fare'].astype(int)
        return X

###############################################################################


class AgeTransformer(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):

        # 计算年龄的平均值
        average_age = X['Age'].mean()
        std_age = X['Age'].std()
        count_na_age = X['Age'].isnull().sum()

        rand_age = np.random.randint(average_age - std_age,
                                     average_age + std_age,
                                     size=count_na_age)

        X['Age'][np.isnan(X['Age'])] = rand_age
        X['Age'] = X['Age'].astype(int)


        return X

###############################################################################


class CabinTransformer(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        # 删除房间号
        X.drop('Cabin', axis=1, inplace=True)
        return X

###############################################################################


class FamilyTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X['Family'] = X['Parch'] + X['SibSp']
        X['Family'].loc[X['Family'] > 0] = 1
        X['Family'].loc[X['Family'] == 0] = 0
        X.drop('Parch', axis=1, inplace=True)
        X.drop('SibSp', axis=1, inplace=True)

        #X['Family'][X['Family'] > 0] = 1
        #X['Family'][X['Family'] == 0] = 0

        return X

###############################################################################


class SexTransformer(BaseEstimator, TransformerMixin):
    def get_persion(self, passanger):
        age, sex = passanger
        return 'child' if age < 16 else sex

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):

        X['Person'] = X[['Age', 'Sex']].apply(self.get_persion, axis=1)

        # 删除掉'sex'
        X.drop('Sex', axis=1, inplace=True)

        sex_dummies = pd.get_dummies(X['Person'])
        sex_dummies.columns = ['Child', 'Female', 'Male']

        # 删除Male 因为存活率太低
        sex_dummies.drop('Male', axis=1, inplace=True)

        X.drop('Person', axis=1, inplace=True)

        X = pd.concat([X, sex_dummies], axis=1)
        return X

###############################################################################


class PclassTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        pclass_dummies = pd.get_dummies(X['Pclass'])
        pclass_dummies.columns = ['Class1', 'Class2', 'Class3']

        # 删除Pclass
        X.drop('Pclass', axis=1, inplace=True)

        X = pd.concat([X, pclass_dummies], axis=1)
        return X


###############################################################################


class PassengerIdTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X.drop('PassengerId', axis=1, inplace=True)
        return X

###############################################################################


class NameTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X.drop('Name', axis=1, inplace=True)
        return X

###############################################################################


class TicketTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X.drop('Ticket', axis=1, inplace=True)
        return X

if __name__ == '__main__':
    X_train = pd.read_csv('../input/train.csv')

    Y_train = X_train['Survived']

    X_train.drop('Survived', axis=1, inplace=True)

    X_train = PassengerIdTransformer().transform(X_train)
    X_train = NameTransformer().transform(X_train)
    X_train = TicketTransformer().transform(X_train)

    print '+' * 80
    print X_train.head()

    em = EmbarkedTransformer()
    X_train = em.fit_transform(X_train)

    print '-' * 80
    print X_train.head()

    ff = FareTransformer()
    X_train = ff.transform(X_train)

    print '+' * 80
    print X_train.head()

    af = AgeTransformer()
    X_train = af.transform(X_train)

    print '-' * 80
    print 'nan age is:', X_train['Age'].isnull().sum()
    print X_train.head()

    cf = CabinTransformer()
    X_train = cf.transform(X_train)
    print '+' * 80
    print X_train.head()

    family_transformer = FamilyTransformer()
    X_train = family_transformer.transform(X_train)
    print '-' * 80
    print X_train.head()

    sex_transformer = SexTransformer()
    X_train = sex_transformer.transform(X_train)
    print '+' * 80
    print X_train.head()

    pclass_transformer = PclassTransformer()
    X_train = pclass_transformer.transform(X_train)
    print '-' * 80
    print X_train.head()
    print '+' * 80
    print Y_train.head()