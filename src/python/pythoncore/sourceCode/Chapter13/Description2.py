# coding: utf-8

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