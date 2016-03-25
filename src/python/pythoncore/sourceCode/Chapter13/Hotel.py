# coding:utf-8

class HotelRoomCalc(object):
    '宾馆我是绿计算器'

    # 注意 这是static的类变量
    version = 1.0

    def __init__(self, rt, sales=0.085, rm=0.1):
        '''Hotel Rool Calc default arguments:
        sales tax == 8.5% and room tax == 10%'''
        self.salesTax = sales
        self.roomTax = rm
        self.roomRate = rt

    def calcTotal(self, days=1):
        'Calculate total: default to daily rate'
        daily = round((self.roomRate * (1 + self.roomTax + self.salesTax)), 2)
        return float(days) * daily

    # 静态方法和类方法,真的看不出来加入 cls 变量有什么意义.
    @staticmethod
    def staticFoo():
        print '这是一个静态方法'

    @classmethod
    def classFoo(cls):
        print '这是一个类方法 %r' % cls


hotel = HotelRoomCalc(1)
print hotel.calcTotal(2)
print hotel.__dict__

HotelRoomCalc.staticFoo()
HotelRoomCalc.classFoo()

print HotelRoomCalc.__base__
