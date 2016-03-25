# coding:utf-8

class HideXX:
    def __init__(self, x):
        self.x = x

    @property
    def x():
        def fget(self):
            return ~self.__x

        def fset(self,x):
            assert isinstance(x,int),\
            '"x" must be an integer!'
            self.__x = ~x

        return locals()

inst4 = HideXX(20)
print inst4.x
inst4.x = 40
print inst4.x

