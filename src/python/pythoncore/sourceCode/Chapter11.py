# coding:utf-8

from time import  ctime, sleep

def tsfunc(func):
    def wrappedFunc():
        print '[%s] %s() called' % (ctime(), func.__name__)
        return func()
    return wrappedFunc


@tsfunc
def foo():
    pass

# 装饰器的理解:
# 上面的代码等同于: foo = tsfunc(foo)
# 1 注意返回值是foo, 也就是说经过tsFunc装饰的原foo变成了新的foo,新的foo是tsfunc(foo)
# 2 tsfunc的返回值,注意是一个函数名.这一点理解很重要,不能写成 "return wrappedFunc()",
# 因为这样写,tsfunc的返回值就不是伊戈尔函数了
# 3 为什么tsFunc的返回值是一个函数.因为foo=tsfunc(foo)说明,tsfunc必须返回一个函数给foo.
# 总结:1 装饰是对某个函数的装饰,装饰完,这个函数的行为就发生了变化,如果再想调用原先的foo该如何处理呢?
# 2: 装饰者返回的是一个函数指针
foo()
sleep(4)

for i in range(2):
    sleep(1)
    foo()