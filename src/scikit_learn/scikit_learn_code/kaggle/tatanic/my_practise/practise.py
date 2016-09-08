# coding:utf-8

import pandas as pd
import dataset
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame, Series
import numpy as np
from sklearn import cross_validation
from sklearn.grid_search import GridSearchCV

HEAD_SWITCH = True
EXPLAIN_DATASET_SWITCH = False

TRAIN_PATH = '../input/train.csv'
TEST_PATH = '../input/test.csv'

titanic_df = pd.read_csv(TRAIN_PATH)
test_df = pd.read_csv(TEST_PATH)

if EXPLAIN_DATASET_SWITCH:
    dataset.describe()

if HEAD_SWITCH:
    #print titanic_df.head()
    print test_df.head()

print titanic_df.info()
print test_df.info()

# 删除掉无效的列
titanic_df = titanic_df.drop(['PassengerId', 'Name', 'Ticket'], axis=1)
test_df = test_df.drop(['Name', 'Ticket'], axis=1)

print titanic_df.head()
print test_df.head()

# 查看某个列的每个值是多少
print type(titanic_df.Embarked.value_counts())
print '-' * 40
print titanic_df.Embarked.value_counts()

# 通过value_counts 知道了embarked 'S'数量最多,所以缺失值使用S替代
titanic_df.Embarked = titanic_df.Embarked.fillna('S')

print titanic_df.Embarked.value_counts()
print titanic_df.info()

print '-' * 40
print titanic_df.Survived[titanic_df.Embarked == 'S'].describe()
print titanic_df.Survived[titanic_df.Embarked == 'C'].describe()

# 下面绘制的原理是 在 Embarked 的 S C Q的分类中的存活率, 图中的 圆点 表示的S/C/Q的均值
# 均值='Survived'==1的数量 / ('Survived'==1 + 'Survived'==0)的数量
# size = 4 aspect=3是表示图的大小 没有这两个参数也可以

# sns.factorplot('Embarked','Survived', data=titanic_df, size=4, aspect=3)


#fig, (axis1,axis2,axis3) = plt.subplots(1,3,figsize=(15,5))

# sns.factorplot('Embarked',data=titanic_df,kind='count',order=['S','C','Q'],ax=axis1)
# sns.factorplot('Survived',hue="Embarked",data=titanic_df,kind='count',order=[1,0],ax=axis2)
#sns.countplot(x='Embarked', data=titanic_df, ax=axis1)
#sns.countplot(x='Survived', hue="Embarked", data=titanic_df, order=[1,0], ax=axis2)

# group by embarked, and get the mean for survived passengers for each value in Embarked
embark_perc = titanic_df[["Embarked", "Survived"]].groupby(['Embarked'],as_index=False).mean()
#sns.barplot(x='Embarked', y='Survived', data=embark_perc,order=['S','C','Q'],ax=axis3)

# Either to consider Embarked column in predictions,
# and remove "S" dummy variable,
# and leave "C" & "Q", since they seem to have a good rate for Survival.

# OR, don't create dummy variables for Embarked column, just drop it,
# because logically, Embarked doesn't seem to be useful in prediction.

embark_dummies_titanic  = pd.get_dummies(titanic_df['Embarked'])

print '-' * 40
print embark_dummies_titanic.head()

embark_dummies_titanic.drop(['S'], axis=1, inplace=True)


print '-' * 40
print embark_dummies_titanic.head()

embark_dummies_test  = pd.get_dummies(test_df['Embarked'])
embark_dummies_test.drop(['S'], axis=1, inplace=True)

titanic_df = titanic_df.join(embark_dummies_titanic)
test_df = test_df.join(embark_dummies_test)

print '+' * 40
print titanic_df.head()

titanic_df.drop(['Embarked'], axis=1, inplace=True)
test_df.drop(['Embarked'], axis=1, inplace=True)

print '-' * 40
print titanic_df.head()

# Fare
#使用均值来填充缺失的值
test_df['Fare'].fillna(test_df['Fare'].mean(), inplace=True)

print '+' * 40
print test_df.info()
print test_df.head()

#将fare从float转换成int
titanic_df['Fare'] = titanic_df['Fare'].astype(int)
test_df['Fare'] = test_df['Fare'].astype(int)

print '-' * 40
print titanic_df.info()
print test_df.info()

# get fare for survived & didn't survive passengers

def fare_analyze(is_plot=True):
    fare_test = titanic_df['Fare']
    print '+' * 40
    print fare_test.head()

    fare_not_survived = titanic_df["Fare"][titanic_df["Survived"] == 0]
    fare_survived = titanic_df["Fare"][titanic_df["Survived"] == 1]

    fare_not_survived = titanic_df['Fare'][titanic_df['Survived'] == 0]
    fare_survived = titanic_df['Fare'][titanic_df['Survived'] == 1]

    # 计算存活和死亡的均值和方差
    avgerage_fare = DataFrame([fare_not_survived.mean(), fare_survived.mean()])
    std_fare = DataFrame([fare_not_survived.std(), fare_survived.std()])

    avgerage_fare = DataFrame([fare_not_survived.mean(), fare_survived.mean()])
    std_fare = DataFrame([fare_not_survived.std(), fare_survived.std()])

    print '-'
    print avgerage_fare
    print std_fare
    # plot
    titanic_df['Fare'].plot(kind='hist', figsize=(15,3), bins=100, xlim=(0,50))

    avgerage_fare.index.names = std_fare.index.names = ["Survived"]

    if is_plot:
        avgerage_fare.plot(yerr=std_fare,kind='bar',legend=False)


# 年龄分析
def age_analyze(is_plot=True):
    '''
    年龄分析
    :return:
    '''


    print 'age', '-'*40
    print titanic_df['Age'].head()

    fig, (axis1, axis2) = plt.subplots(1, 2, figsize=(15, 4))
    axis1.set_title(u'原始的年龄数据')
    axis2.set_title(u'新的年龄')

    # 计算年龄均值和方差
    average_age_titanic = titanic_df['Age'].mean()
    std_age_titanic = titanic_df['Age'].std()

    # 计算年龄中为NaN的数量
    count_nan_age_titanic = titanic_df['Age'].isnull().sum()

    # 获取测试数据集的 均值 方差 和 nan
    average_age_test = test_df['Age'].mean()
    std_age_test = test_df['Age'].std()
    count_nan_age_test = test_df['Age'].isnull().sum()

    print 'train nacount %d, test na count %d' % (count_nan_age_titanic, count_nan_age_test)

    # 用均值和方差产生随机值 (mean-std) & (mean+std)
    # 这是产生一个随机值的数组用来随机的填充进入到 nan 的数据中
    # 这比单独使用 mean 单一值更好 因为 使用了在标准差上下的随机值

    rand_1 = np.random.randint(average_age_titanic - std_age_titanic,
                               average_age_titanic + std_age_titanic,
                               size=count_nan_age_titanic)

    rand_2 = np.random.randint(average_age_test - std_age_test,
                               average_age_test + std_age_test,
                               size=count_nan_age_test)

    #print 'rand1: %d, rand2: %d' % (rand_1, rand_2)



    # 绘制原始的年龄值
    # 注意:删除所有的 空值 并且转换成int
    titanic_df['Age'].dropna().astype(int).hist(bins=70, ax=axis1)


    # fill NaN 值 使用随机值
    titanic_df['Age'][np.isnan(titanic_df['Age'])] = rand_1
    test_df['Age'][np.isnan(test_df['Age'])] = rand_2


    # 将数据从float转换成int
    titanic_df['Age'] = titanic_df['Age'].astype(int)
    test_df['Age'] = test_df['Age'].astype(int)

    # 绘制新的Age
    titanic_df['Age'].hist(bins=70, ax=axis2)

    # 继续绘制不同的年龄段对标签 'Surviced'的曲线图


    if is_plot:
        facet = sns.FacetGrid(titanic_df,
                              hue='Survived',
                              aspect=2)
        facet.map(sns.kdeplot, 'Age', shade=True)
        facet.set(xlim=(0, titanic_df['Age'].max()))
        facet.add_legend()

    # 计算不同的年龄段下的存活率

    fig, axis1 = plt.subplots(1, 1, figsize=(18, 4))
    # 以分组的方法来计算每个年龄下的均值,因为suvive=1 是存活率
    average_age = titanic_df[['Age', 'Survived']].groupby('Age', as_index=False).mean()
    print type(average_age)
    print average_age

    if is_plot:
        sns.barplot(x='Age', y='Survived', data=average_age)


def cabin_analyze(is_plot=True):
    print '-' * 40
    print titanic_df['Cabin']
    print titanic_df['Cabin'][titanic_df['Cabin'].notnull()].count()

    # 房间号 没有意义所以直接删除该列
    titanic_df.drop('Cabin', axis=1, inplace=True)
    test_df.drop('Cabin', axis=1, inplace=True)

    print titanic_df.head()
    print test_df.head()

def family_analyze(is_plot=True):
    # 将父母和兄弟姐妹整合成一个特征
    titanic_df['Family'] = titanic_df['Parch'] + titanic_df['SibSp']
    print titanic_df['Family'].head(n=20)

    family_no = titanic_df['Family'].loc[titanic_df['Family'] > 0]
    print type(family_no)
    print family_no.head()
    family_no_1 = titanic_df['Family'][titanic_df['Family'] > 0]
    print type(family_no_1)
    print family_no_1.head()

    # 有家庭的设置为1 无家庭成员的设置成0
    titanic_df['Family'].loc[titanic_df['Family'] > 0] = 1
    titanic_df['Family'].loc[titanic_df['Family'] == 0] = 0

    #同样的方式处理测试集
    test_df['Family'] = test_df['Parch'] + test_df['SibSp']

    test_df['Family'].loc[test_df['Family'] > 0] = 1
    test_df['Family'].loc[test_df['Family'] == 0] = 0

    # 将'Parch'和'SibSp' 删除
    titanic_df.drop(['Parch', 'SibSp'], axis=1, inplace=True)
    test_df.drop(['Parch', 'SibSp'], axis=1, inplace=True)

    print '-' * 40
    print titanic_df.head()
    print test_df.head()

    # 绘制 'Family'的数量在0,1上面

    fig, (axis1, axis2) = plt.subplots(1, 2, sharex=True, figsize=(10,5))

    if is_plot:
        # 绘制count plot
        sns.countplot(x='Family', data=titanic_df, order=[0,1],ax=axis1)

    # 在 family='0' 或者 '1'的时候, surviced的情况
    family_perc = titanic_df[['Family', 'Survived']].groupby('Family', as_index=False).mean()


    if is_plot:
        sns.barplot(x='Family', y='Survived', data=family_perc, order=[0,1], ax=axis2)
        axis1.set_xticklabels([u'有家庭', u'孤身一人'], rotation=0)


def get_persion(passenger):
    age, sex = passenger
    return 'child' if age < 16 else sex

def sex_analyze(is_plot=True):
    '''
    性别分析 将性别按照 male, fmale, child
    :return
    '''
    global  titanic_df
    global test_df

    titanic_df['Person'] = titanic_df[['Age', 'Sex']].apply(get_persion, axis=1)
    test_df['Person'] = test_df[['Age', 'Sex']].apply(get_persion, axis=1)

    print '-' * 40
    print titanic_df.head(n=20)
    print test_df.head(n=20)

    # 将 'Sex' 删除
    titanic_df.drop(['Sex'], axis=1, inplace=True)
    test_df.drop(['Sex'], axis=1, inplace=True)

    # 创建基于person的dummy向量
    # 删除掉 'Male'的原因是 'Male'有较低的存活率 所以这个因子起到的作用不大
    person_dummies_titanic = pd.get_dummies(titanic_df['Person'])
    person_dummies_titanic.columns = ['Child', 'Female', 'Male']
    person_dummies_titanic.drop(['Male'], axis=1, inplace=True)

    person_dummies_test = pd.get_dummies(test_df['Person'])
    person_dummies_test.columns = ['Child', 'Female', 'Male']
    person_dummies_test.drop(['Male'], axis=1, inplace=True)

    titanic_df = titanic_df.join(person_dummies_titanic)
    test_df = test_df.join(person_dummies_test)

    fig, (axis1, axis2) = plt.subplots(1, 2, figsize=(10, 5))

    if is_plot:
        # 绘制person的数量
        sns.countplot(x='Person', data=titanic_df, ax=axis1)

    if is_plot:
        # 绘制存活率
        person_perc = titanic_df[['Person', 'Survived']].groupby('Person', as_index=False).mean()
        sns.barplot(x='Person', y='Survived', data=person_perc,
                    ax=axis2,
                    order=['male', 'female', 'child'])

    # 将person扔掉
    titanic_df.drop(['Person'], axis=1, inplace=True)
    test_df.drop(['Person'], axis=1, inplace=True)


def pclass_analyze(is_plot=True):
    global titanic_df
    global test_df

    print '-' * 40
    print titanic_df['Pclass'][(titanic_df['Pclass'] == 1) & (titanic_df['Survived'] == 1)].count()
    print titanic_df['Pclass'][(titanic_df['Pclass'] == 1) & (titanic_df['Survived'] == 0)].count()
    print titanic_df['Survived'][titanic_df['Pclass'] == 1].describe()
    print titanic_df['Survived'][titanic_df['Pclass'] == 2].describe()
    print titanic_df['Survived'][titanic_df['Pclass'] == 3].describe()

    if is_plot:
        sns.factorplot('Pclass', 'Survived',
                       order=[1,2,3],
                       data=titanic_df,
                       size=5)

    # 创建pclass的向量化数据
    pclass_dummies_titanic = pd.get_dummies(titanic_df['Pclass'])
    pclass_dummies_titanic.columns = ['Class_1', 'Class_2', 'Class_3']
    pclass_dummies_titanic.drop(['Class_3'], axis=1, inplace=True)

    pclass_dummies_test = pd.get_dummies(test_df['Pclass'])
    pclass_dummies_test.columns = ['Class_1', 'Class_2', 'Class_3']
    pclass_dummies_test.drop(['Class_3'], axis=1, inplace=True)

    titanic_df.drop(['Pclass'], axis=1, inplace=True)
    test_df.drop(['Pclass'], axis=1, inplace=True)

    titanic_df = titanic_df.join(pclass_dummies_titanic)
    test_df = test_df.join(pclass_dummies_test)




age_analyze(False)
cabin_analyze(False)
family_analyze(False)

sex_analyze(False)
pclass_analyze(False)

print '-' * 40
print titanic_df.head()
print test_df.head()

# 生成训练集和测试集
X_train = titanic_df.drop('Survived', axis=1)
Y_train = titanic_df['Survived']
X_test = test_df.drop('PassengerId', axis=1).copy()

print '+' * 40
print X_train.head()
print Y_train.head()
print X_test.head()

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

def train_lr():
    '''
    使用LR算法进行训练
    :return:
    '''

    print u'X_trian, Y_train type:', type(X_train), type(Y_train)
    logreg = LogisticRegression()
    logreg.fit(X_train, Y_train)
    Y_pred = logreg.predict(X_test)

    score = logreg.score(X_train, Y_train)
    print '-' * 40
    print u'逻辑回归分数 %f' % score

    # 打印逻辑回归的相关feature的系数
    coeff_df = DataFrame(titanic_df.columns.delete(0))
    coeff_df.columns = ['Features']
    print coeff_df

    coeff_df[u'相关系数'] = pd.Series(logreg.coef_[0])

    print coeff_df

    return Y_pred


def train_random_forest():
    random_forest = RandomForestClassifier(n_estimators=100)
    random_forest.fit(X_train, Y_train)
    Y_pred = random_forest.predict(X_test)

    score = random_forest.score(X_train, Y_train)
    print u'随机森林的分数 %f' % score

    return Y_pred


def train_lr_by_cv():
    print u'X_trian, Y_train type:', type(X_train), type(Y_train)

    logreg = LogisticRegression(C=0.5)
    score = cross_validation.cross_val_score(logreg, X_train, Y_train, cv=10, n_jobs=-1)


    print ('train_lr_by_cv' + '-----------------------')
    print score
    print 'mean: %.2f, std: %.2f' % (score.mean(), score.std())
    pass


def train_lr_by_gridsearch():
    print u'X_trian, Y_train type:', type(X_train), type(Y_train)

    tune_params = [{'C':[0.1, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 2, 3, 4, 5]}]
    logreg = LogisticRegression()
    clf = GridSearchCV(logreg, tune_params, cv=5, n_jobs=-1)
    clf.fit(X_train, Y_train)

    print 'train_lr_by_gridsearch', '-' * 40
    print 'best score: %.2f' % (clf.best_score_)
    print 'best param: ', clf.best_params_
    print clf.grid_scores_


def train_random_forest_by_cv():
    random_forest = RandomForestClassifier(n_estimators=100)
    score = cross_validation.cross_val_score(random_forest, X_train, Y_train, cv=10, n_jobs=-1)
    print ('train_random_forest_by_cv' + '-----------------------')
    print score
    print 'mean: %.2f, std: %.2f' % (score.mean(), score.std())


train_lr_by_cv()
train_random_forest_by_cv()

train_lr_by_gridsearch()

Y_pred = train_random_forest()
Y_pred = train_lr()

print 'Y_pred:type: ', type(Y_pred)
# 产生最终的预测结果并期缴
submission = pd.DataFrame({'PassengerId':test_df['PassengerId'],
                           'Survived':Y_pred})
submission.to_csv('titanic_pred.csv', index=False)
#plt.show()