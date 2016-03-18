# Chapter4

## type函数
类型也是对象，所以type()返回的是一个类型对象，而不是一个字符串。

## 列表逆向输出

```
foostr = 'abcdef'
print foostr[::-1]

输出:
fedcba
```

## is进行对象指针的比较

```
x = [1, 2, 3, 4]
y = x
z = [1, 2, 3, 4]

print x is y
print x is z
print x is not y

输出:
True
False
False
```

## 布尔运算符
and or not

## 几个有用的内建函数
cmp(obj1, obj2) 比较。

str() # 致力于获取到一个对象的好的字符串表述。所以无法使用 eval()函数来重新建立该对象。

repr() # 该函数返回对象的字符串形式。可以使用eval()来重建对象.

` ` 操作符与repr()函数功能一致。

## python是不支持函数重载的。

## isInstance和type的用法

```
def displayNumType(num):
    print num, 'is',

    if isinstance(num, (int, long, float, complex)):
        print 'a number of type:', type(num).__name__
    else:
        print 'not a number at all'

displayNumType(-69)

输出:
-69 is a number of type: int
```

isInstance与java中是一样的。type则负责输出该类型的名字。

## 类型工厂
int() 事实上int是类，所以int()是个方法。

## Python的内建类型


| 数据类型 | 存储模型 | 更新模型 | 访问模型 |
| --------|--------|---------|---------|
| 数字 | Scalar | 不可更改 | 直接访问 |
| 字符串 | Scalar | 不可更改 | 顺序访问 |
| 列表  | Container | 可更改 |  顺序访问 |
| 元组 | Container | 不可更改 | 顺序访问 |
| 字典 | Container | 可更改 | 映射访问 |## 不支持的类型
char, byte. Python没有float和double两种类型，只有double. 另外，还有一种Decimals用的任意精度的数值，用来处理金钱这类数据很有用。      