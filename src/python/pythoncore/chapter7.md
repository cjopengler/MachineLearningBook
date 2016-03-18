# Chapter7 映射和集合类型
字典也就是Java的hashtable，使用{}来表示。列表是[]元组是().

## 字典的创建
```

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

输出:

{}
{'name': 'earth', 'port': 80}
{'y': 2, 'x': 1}
{'y': -1, 'x': -1}
{'foo': None, 'bar': None}
```

## 集合

```
集合操作:
# coding:utf-8

# 创建集合,可变集合不要求一定可hash
aset = set('abcde')
print aset

# 集合的操作
aset.add('q')
aset.add(123)

print aset

# 创建不可变集合. 不可变集合必须是可哈希的
bfrozen = frozenset('abcdef')

print bfrozen

# 集合支持 交 并 补 和 差分
bset = set('uabc')

print aset | bset
print aset & bset
print aset - bset
print aset ^ bset

输出:
set(['a', 'c', 'b', 'e', 'd'])
set(['a', 'c', 'b', 'e', 'd', 'q', 123])
frozenset(['a', 'c', 'b', 'e', 'd', 'f'])
set(['a', 'c', 'b', 'e', 'd', 'q', 'u', 123])
set(['a', 'c', 'b'])
set(['q', 123, 'e', 'd'])
set(['q', 'e', 'd', 'u', 123])

```
