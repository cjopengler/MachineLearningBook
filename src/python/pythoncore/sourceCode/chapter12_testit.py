# coding: utf-8

def testit(func, *nkwargs, **kwargs):
    'func 函数指针; 后面的参数可以适应任意函数的参数'

    try:
        retval = func(*nkwargs, **kwargs)
        result = (True, retval)

    except Exception, diag:
        result = (False, str(diag))

    return result

def test():
    funcs = (int, long, float)
    vals = (1234, 12.34, '1234', '12.34')

    for eachFunc in funcs:
        print '_'*20
        for eachVal in vals:
            retval = testit(eachFunc, eachVal)

            if (retval[0]):
                print '%s(%s) = ' % (eachFunc.__name__, str(eachVal)), retval[1]
            else:
                print '%s(%s) = Failed ' % (eachFunc.__name__, str(eachVal)), retval[1]

test()

# lambda表达式,就相当于函数y是默认参数2, 这种方式能够提升性能.
# 但是为什么会提升性能我还不知道
a = lambda x, y=2: x+y
print a(3), a(3, 5)

from random import randint
def odd(n):
    return n%2

allNums = []

for eachNum in range(9):
    allNums.append(randint(1, 99))

print filter(odd, allNums)

# odd 函数极其简单可以使用lambda替换


for eachNum in range(9):
    allNums.append(randint(1, 99))

print filter(lambda n: n%2, allNums)

# filter会被列表解析式替换掉. 最终filter是注定要被淘汰的

print [n for n in allNums if n%2]

# 上面的代码最后allNums也可以省略 最终变成一句话.这种表达式也太犀利了.
print [n for n in [randint(1, 99) for i in range(9)] if n%2]

# 在上面的例子中对列表解析式应该更多的了解 exp for... if ...,
# 最后生成数组是 exp 并且受到 if限定的结果.

# map函数是映射的意思,也就是将一个序列中所有的元素经过map指定的函数进行映射成一个新的序列

print map ((lambda x:x+2), [0, 1 ,2 ,3 , 4])

# map函数作用在多个序列上的思想是: map(func, seq1, seq2, ..., seqn)
# 执行的结果是 一个列表(不是元组):
#  [func((seq1[0], seq2[0], ..., seqn[0])),
#   func((seq1[1], seq2[1], ..., seqn[1])),
#  ...
#   func((seq1[m], seq2[m], ..., seqn[m]))]

print map (lambda x, y:x+y, [1,3,5], [2,4,6])

# reduce将序列所有的值变成一个,所以reduce的函数必须是一个二元函数
print 'reduce计算和:', reduce((lambda x,y:x+y), range(5))

# 偏函数这是一个新的概念
# 偏函数是创建一种函数调用的别名
# 这种方法的好处是可以将使用一大堆参数的函数简化使用

from operator import add,mul
from functools import  partial

add1 = partial(add, 1)

print '偏函数计算 %d' % add1(10)
