# coding:utf-8

class P(object):
    def foo(self):
        print 'I am p foo'

class C(P):
    def foo(self):
        P.foo(self)
        self.abc = 'abc'
        print 'I am c foo'

    def __str__(self):
        return 'This is a C'

c = C()

print c
c.foo()



print isinstance(c, C)
print issubclass(C, P)

print hasattr(c, 'bar')

print getattr(c, 'abc')

setattr(c, 'new_attr', '这是一个新的属性')
print c.new_attr, getattr(c, 'new_attr')

delattr(c, 'new_attr')
print hasattr(c, 'new_attr')

# vars 以字典的形式列出对象中的属性和值
print c.__dict__
print vars(c)
