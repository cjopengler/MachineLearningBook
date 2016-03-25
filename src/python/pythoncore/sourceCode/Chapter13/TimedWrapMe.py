# coding:utf-8

from time import time, ctime

class TimeWrapMe(object):
    '''对其他对象的创建和访问的时间包装器'''

    def __init__(self, obj):
        # 注意下面的使用的前置__ 表示私有数据
        self.__data = obj
        self.__ctime = self.__mtime = \
            self.__atime = time()

    def set(self, obj):
        self.__data = obj
        self.__mtime = self.__atime = time()

    def get(self):
        self.__atime = time()
        return self.__data

    def gettimeval(self, t_type):
        # 先验证是否是字符类型
        if type(t_type) != type('') or \
            t_type[0] not in 'cma':
            raise TypeError,\
                '''参数错误,必须是 'c','m'或者'a' '''
        # 注意下面这句话的含义是将一个字符串转换成了一个对象
        # 这个字符串是 self.TimeWrapMe.atime 或者 .ctime 或者 .mtime
        # 就这样建字符串转换成了对象,类似于序列化
        return eval('self._%s__%stime' % (self.__class__.__name__, t_type[0]))

    def gettimestr(self, t_type):
        return ctime(self.gettimeval(t_type))

    def __repr__(self):
        self.__atime = time()
        return `self.__data`

    def __str__(self):
        self.__atime = time()
        return str(self.__data)

    def __getattr__(self, attr):
        self.__atime = time()
        return getattr(self.__data, attr)

timeWrappedObj = TimeWrapMe(932)
print timeWrappedObj.gettimestr('c')

