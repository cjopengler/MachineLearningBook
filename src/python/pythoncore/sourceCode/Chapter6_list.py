# coding:utf-8

alist = [123, 'abc']

print alist

# 字符串追加
alist.append('ggg')

print alist

# 字符串删除
alist.remove(123)

print alist

# 字符串可以直接进行比较
blist =[456, 'ddd']

print alist < blist

# 列表类似的多维数组
matrix = [[1, 2, 3], [4, 5, 6]]

print matrix

# 列表可以相加
clist = alist + blist

print clist

# 列表的extend函数可以将一个新的列表添加到当前列表尾部
clist.extend(['lll', 99])

print clist

# 显性和隐性元组
x, y = 1, 2

(a, b) = (3, 4)
print x, y, a, b
