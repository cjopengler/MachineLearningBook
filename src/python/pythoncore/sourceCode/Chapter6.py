# coding:utf-8

s = 'abcde'

negtiveRange = range(-1, -len(s) - 1, -1)
positiveRange = range(0, len(s))

print s
for i in negtiveRange:
    print 's[%d]:%s' % (i, s[i]),

print '\n'
for i in positiveRange:
    print 's[%d]:%s' % (i, s[i]),

print '\n'

negtiveRange = [None] + negtiveRange

print s[0:len(s)+1]
print s[0:None]
print s[-1:-len(s)-1:-1]
print s[-1:None:-1]

print negtiveRange
for i in negtiveRange:
    print s[:i]

s = u'你好'
print s

print  str(range(4))

x = 'abc'
y = 'aBc'

print x < y

# 判断字符串是否包含另外的字符串
print 'ab' in 'cabde', 'ab' not in '123'

strJ = '%s%s' % ('ab', 'cd')
print strJ

strJ2 = ''.join(('abddd', 'cd'))
print strJ2

print 'kkk''jjj'

print r'\n'

print zip('abc', '123')