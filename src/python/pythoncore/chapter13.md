# Chapter13 类

## 接口是如何体现的？

## 多态

```
# coding:utf-8

class P(object):
    def foo(self):
        print 'I am p foo'

class C(P):
    def foo(self):
        P.foo(self)
        print 'I am c foo'

c = C()

c.foo()
```

看看 ```c=C()``` 按照Java应该是 ```P c = new C()``` ，但是因为python不需要写类型。所以 ``` c = C() ``` 这就是多态的表示了.

这里要注意一点，当覆盖```__init__```的时候不要忘记调用父类的```__init__```.

## 动态添加属性
这个有点夸张呀。

## 关于private,public,protected
Python中是没有这些关键字的。通过 __Attr 这种方式来混淆Attr属性，实际上是被混淆成了额 ```__ClassName_Attr```，所以这种混淆本质上意义不大，但是可以有效的区分，父类和子类的同一个属性。

另外在模块中的单下划线的好处是，当模块被加载的时候 属性不会被执行。

## 描述符
描述符是针对属性的，是属性的一个代理。"get"获取,"set"修改,"delete"删除.就是实现类中的 ```__get__, __set__ 和 __delete__```。
而我们真正需要的是类似java的getter和setter，那么这是通过 property来实现的。避免使用描述符。

```
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

输出:
attmpt to assing 'bar' ... ignoring
Accessing attribe ... ignoring
get_x is called
set_x is called
```

使用下面的技巧更加容易实现getter和setter

```
# 先前的propterty 使得getX和setX能够被外部调用,下面的技巧将避免这个问题

class HideX(object):
    def __init__(self, x):
        self.__x = ~x

    @property
    def x(self):
        return ~self.__x

    @x.setter
    def x(self, val):
        self.__x = ~val


h = HideX(2)

print h.x
```

## 关于抽象类和接口
参考: [抽象类和接口](http://blog.csdn.net/kobeyan/article/details/44344087)