# coding:utf-8

# 声明一个空的字典
dict1 = {}

# 声明有数据的字典
dict2 = {'name':'earth', 'port':80}

# 使用dict()工厂方法来创建字典, 参数是元组
fdict = dict((['x',1], ['y', 2]))

# 使用frmokeys来创建默认字典
ddict = {}.fromkeys(('x', 'y'), -1)

edict = {}.fromkeys(('foo', 'bar'))

print dict1
print dict2
print fdict
print ddict
print edict

# 循环遍历字典

for key in dict2:
    print 'key=%s, value=%s' % (key, dict2[key])

print dict2.items()
# 判断key是否在字典中

print 'server' in dict2

# 字典中删除一个元素
print dict2.pop('port')

# 代码解析: 'xy'[i-1], 'xy'表示字符串,[i-1]表示字符串的下标
print dict([('xy'[i-1], i) for i in range(1,3)])

# 另外一种创建字典的方法
print dict(x=1, y=2)

# 对字典的key排序
print dict2
dict2['a'] = 1
dict2['b'] = 2

print sorted(dict2)