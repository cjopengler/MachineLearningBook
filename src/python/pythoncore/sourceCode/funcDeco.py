#!usr/bin/evn python
# coding:utf-8

from time import time

# 知识点介绍:
# 1 内嵌函数
def logged(when):
    def log(f, *args, **kargs):
        print '''调用:函数:%s args:%r kargs:%r''' % (f, args, kargs)

    def pre_logged(f):
        def wrapper(*args, **kargs):
            log(f, *args, **kargs)
            return f(*args, **kargs)
        return wrapper

    def post_logged(f):
        def wrapper(*args, **kargs):
            now = time()

            try:
                return f(*args, **kargs)
            finally:
                log(f, *args, **kargs)
                print ' time delta:%s' % (time() - now)

        return wrapper

    try:
        # 下面的语句使用了字典来代替 switch语句是值得学习的.
        return {'pre':pre_logged, 'post': post_logged}[when]
    except KeyError, e:
        raise  ValueError(e), '''must be "pre" or "post"'''

# 函数的装饰 相当于 hello = logged("post")(hello)
# 注: logged("post")返回了 post_logged,而后 hello = post_logged(hello)
@logged("post")
def hello(name):
    print "Hello,", name

hello("World!")