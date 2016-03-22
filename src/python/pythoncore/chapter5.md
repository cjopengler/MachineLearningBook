# Chapter5
## 除法
"/" 和 "//"的区别。"/"现在的性质与Java是一样的，"//"的结果是去掉小数部分，返回一个最接近的整数。

```
# from __future__ import  division
a = 1/2
b = 1 // 2
c = 1.0 / 2.0
d = 1.0 // 2.0
e = -1 // 2
f = -1 / 2
print a, b, c, d, e, f

输出:
0 0 0.5 0.0 -1 -1
```

看到最上面注释掉的,如果打开:

```
from __future__ import  division
a = 1/2
b = 1 // 2
c = 1.0 / 2.0
d = 1.0 // 2.0
e = -1 // 2
f = -1 / 2
print a, b, c, d, e, f

输出:
0.5 0 0.5 0.0 -1 -0.5
```

如果加上上面的引用，那么 "/"则执行真正的除法。

## 位运算
位运算与C语言是一样的。

## 一些对数值进行处理的内建函数

```
m = coerce(1.1, 11L)

print abs(-1), coerce(1.3, 134L), m[1], divmod(10, 3), pow(2, 5),round(3.45, 2)

输出:

1 (1.3, 134.0) 11.0 (3, 1) 32 3.45
```

round 计算四舍五入，以及小数点后面几位。

| 函数 | 功能 |
| ----- | -----|
| hex(num) | 将数字转换成十六进制数并以字符串形式返回 oct(num) 将数字转换成八进制数并以字符串形式返回 |
| chr(num) | 将ASCII值的数字转换成ASCII字符,范围只能是0 <= num <= 255。|
| randrange() | 它接受和 range()函数一样的参数, 随机返回range([start,]stop[,step])结果的一项 |

## 十进制数据

```
from decimal import  Decimal
dec = Decimal('.1')

print dec, dec + Decimal('1.0')
```

注意 dec = Decimal(.1) 是不对的，必须使用字符串。这很好理解，因为Decimal是语言本身定义出来的，所以使用double进行转换，也是无法转换的。

## 随机