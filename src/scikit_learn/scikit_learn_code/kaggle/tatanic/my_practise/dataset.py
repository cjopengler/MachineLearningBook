# coding:utf-8

def describe():
    '''
    解释数据集各个column的含义
    :return:
    '''
    descibe_list = [(u'PassengerId', u'旅客ID'),
                    (u'Survived', u'是否活下来了，1:yes  0:no. 标签'),
                    (u'Pclass', u'旅客等级 1 2 3 分别代表不同的等级,那个等级高呢?'),
                    (u'Name', u'名字'),
                    (u'Sex', u'性别'),
                    (u'Age', u'年龄'),
                    (u'SibSp', u'有多少兄弟姐妹/配偶同船'),
                    (u'Parch', u'有多少父母/子女同船'),
                    (u'Ticket', u'船票号码'),
                    (u'Fare', u'船票收费'),
                    (u'Cabin', u'所在房间'),
                    (u'Embarked', u'登船城市 C Q S 分别代表不同的城市')
                    ]

    for desc in descibe_list:
        print '%s\t%s' % (desc[0], desc[1])