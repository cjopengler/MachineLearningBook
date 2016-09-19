# coding:utf-8
"""
release版本,使用标准的scikit-learn操作步骤
"""

import pandas as pd
from pandas import DataFrame
from pandas import Series
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.grid_search import GridSearchCV

from tatanic_transformer import *
from tatanic_transformer_v2 import *


if __name__ == '__main__':

    df = pd.read_csv('../input/train.csv')

    y_train = df['Survived']
    X_train = df.drop('Survived', axis=1)

    lr = LogisticRegression()
    """
    clf = Pipeline([('passengerid', PassengerIdTransformer()),
                    ('pclass', PclassTransformer()),
                    ('name', NameTransformer()),
                    ('sex', SexTransformer()),
                    ('age', AgeTransformer()),
                    ('family', FamilyTransformer()),
                    ('ticket', TicketTransformer()),
                    ('fare', FareTransformer()),
                    ('cabin', CabinTransformer()),
                    ('embarked', EmbarkedTransformer()),
                    ('lr', lr)
                    ])



    tune_params = {'lr__C': [0.1, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 2, 3, 4, 5],
                   'lr__solver':['newton-cg', 'lbfgs', 'liblinear', 'sag']}
    """

    clf_v2 = Pipeline([('passengerid', PassengerIdTransformer()),
                       ('pclass', PclassTransformer()),
                       ('name', NameTransformer()),
                       ('sex', SexTransformerV2()),
                       ('age', AgeTransformV2()),
                       ('family', FamilyTransformer()),
                       ('ticket', TicketTransformer()),
                       ('fare', FareTransformer()),
                       ('cabin', CabinTransformer()),
                       ('embarked', EmbarkedTransformer()),
                       ('lr', lr)
                       ])
    tune_params = {'lr__C': [0.1, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 2, 3, 4, 5],
                   'lr__solver': ['newton-cg', 'lbfgs', 'liblinear']}

    grid_search = GridSearchCV(clf_v2, tune_params, cv=5, n_jobs=-1)
    grid_search.fit(X_train, y_train)

    print 'best:', grid_search.best_params_
    print 'best:', grid_search.best_score_

    X_test = pd.read_csv('../input/test.csv')
    passenger_id = X_test['PassengerId']

    y_pred = grid_search.predict(X_test)
    # 产生最终的预测结果并期缴
    submission = pd.DataFrame({'PassengerId': passenger_id,
                               'Survived': y_pred})
    submission.to_csv('titanic_pred_v2.csv', index=False)




