# Chapter3

## 特殊符号
"\\" 连接上下两行。

```
a = 3 \
    + 2
print a
```

## 赋值
多元赋值,可以处理C语言中 x, y使用临时变量互相赋值的case.

```
(x, y, z) = (1, 2, 'abc')

print "x=%d, y=%d, z=%s" % (x, y, z)

(x, y) = (y, x)

print "x=%d, y=%d, z=%s" % (x, y, z)

输出:
x=1, y=2, z=abc
x=2, y=1, z=abc
```

## name属性
对于一个模块来说，如果想要被执行，将 ```__ name__ = main```，而如果只是被调用，那么 ```___name__ = 模块名```.

