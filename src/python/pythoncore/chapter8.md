# Chapter8 条件和循环

在这一章，最应该搞清楚的就是列表解析和生成器。

```
# coding:utf-8

# 三元表达式

x = 1
y = 2

smaller = x if x < y else y

print smaller

# 索引和数据同时获取 enumerate()

nameList = ['Jhone', 'Shirley', 'Ben']

for (i, eachLee) in enumerate(nameList):
    print '%d %s Lee' % (i+1, eachLee)

# 空语句 pass的代替.类似下面的语法,如果去掉pass,会显示错误的.

if True :
    pass
else:
    pass

# for ... else; while ... else 会在循环break跳出的时候是不会执行的,只有非break跳出才会执行.
# 这很好理解,break跳出是因为发生了问题,那么问题的处理就应该在break的时候处理
# 没有发生任何问题才会进入到else处理.
# 换句话说 break处理错误, else处理正确.

i = 3

while i > 0:
    if (i > 4):
        print 'in break %d' % i
        break;
    i = i -1
    print 'while', i

else:
    print 'break for else'

# 迭代器使用 next来访问
nameIt = iter(nameList)

while True:
    try:
        name = nameIt.next()
        print name

    except StopIteration:
        break

# 文件迭代器

myFile = open('log.txt')

for eachLine in myFile:
    print eachLine

myFile.close()

# 列表解析 重中之重 [expr for iter_var in iterable]
# 列表解析的表达式取代内建的map以及lamda 效率更高
print [x**2 for x in range(6) if x % 2]

print [(x+1, y+1) for x in range(3) for y in range(5)]

x = [1, 2, 3, 4]

# 计算文件中的所有单词数目,下面使用的是生成器表达式,比列表解析效率更好

myFile = open('log.txt')

print sum(len(word) for line in myFile for word in line.split())

myFile.close()

# 列表解析和生成器 是 python有别于其他语言的根本区别

# 输出

/System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7 /Users/panxu/PycharmProjects/PythonCore/Chapter8.py
1
1 Jhone Lee
2 Shirley Lee
3 Ben Lee
while 2
while 1
while 0
break for else
Jhone
Shirley
Ben
Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

Fatal Error: invalid input

[1, 9, 25]
[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5)]
1081

Process finished with exit code 0

```