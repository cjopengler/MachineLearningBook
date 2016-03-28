# coding:utf-8

import numpy as np
persontype = np.dtype({
    'names':['name', 'age', 'weight'],
    'formats':['S32','i', 'f']})
a = np.array([("Zhang",32,75.5),("Wang",24,65.2)],
    dtype=persontype)

print a

def foo():
    def atholder(f):
        print f
        return f
    return atholder

@foo()
def hello():
    print 'hello'

hello()

print '... dec'
def dec():
    def wraper(f):
        print 'dec is called'
        return f

    return wraper

@dec()
def f():
    print 'f is called'

f()



print '... decarg'


def decarg(a, b):
    print 'decarg is called', a, b

    def wraper(func):
        def test(a, b):
            print 'test is called', a, b
            return func()

        return test

    return wraper

@decarg('a','b')
def farg():
    print 'farg is called'
    return 3

print farg('a', 'b')
