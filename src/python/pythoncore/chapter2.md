# Chapter2
## 字符串操作

字符串的索引从0开始，最后一个是-1. [begin:end] 这种表述的区间是 [begin, end).

```
myString = 'HelloWorld'
print myString

print "string test: %c %c %s %s %s" % (myString[0], myString[-1], myString[1:3], myString[0:], myString[:-1])
```

输出结果:

```
string test: H d el HelloWorld HelloWorl
```

```
powerString = 'abc'*3
输出:
abcabcabc
```
这种表示可以用来划出分割线。