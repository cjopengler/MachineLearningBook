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

