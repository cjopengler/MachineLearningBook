# coding:utf-8

# *表示的是可变参数
def tupleVarArgs(arg1, arg2='defaultb', *theRest):
    '展示可变参数'
    print 'formal arg1: ', arg1
    print 'formal arg2:', arg2
    for eachXtrArg in theRest:
        print 'another arg:', eachXtrArg

tupleVarArgs('abc')

tupleVarArgs('abc', 123, 'xyz', 456)

# **表示的是字典型的可变参数

def dictVarArgs(arg1, arg2='defualtB', **theRest):
    'display 2 regular args and keyword variable args'
    for eachXtrArg in theRest.keys():
        print 'Xtra arg %s: %s' % (eachXtrArg, str(theRest[eachXtrArg]))

dictVarArgs(1220, 740, c='grail')
