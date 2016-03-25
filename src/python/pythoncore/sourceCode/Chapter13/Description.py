# coding:utf-8

class DevNull2(object):
    def __get__(self, instance, owner):
        print 'Accessing attribe ... ignoring'

    def __set__(self, instance, value):
        print 'attmpt to assing %r ... ignoring' % (value)

class C2(object):
    foo = DevNull2()

    def __init__(self, x):
        assert isinstance(x, int), \
        '''"x" must bie an integer'''

        self.__x = ~x

    def get_x(self):
        print 'get_x is called'
        return ~self.__x

    def set_x(self, val):
        print 'set_x is called'
        self.__x = ~val

    x = property(get_x, set_x)


c2 = C2(5)

# 下面是对foo进行赋值,那么就会默认执行 __set__
c2.foo = 'bar'

# 下面是获取foo,也就是会调用 __get__
x = c2.foo

# 这里的描述符和Java是有些区别的,与getter和setter
# Java中是写在C的类中,对foo进行封装,而这里是对foo所属的类进行封装

# 类似于java中的封装是 propterty这个函数的处理
a = c2.x
c2.x = 9


