# 实战技巧
## Unicode的处理
在使用python处理文本的时候，存在各种不同的编码方式。可能是gbk,utf-8以及acii.对于python的字符串来说，本质是存储的是字节码，注意是字节码。那么utf-8只是将多个字节码组织在一起的一种新的表现形式。明白这个道理，就很容易明白了。

```
a = '你好'

print a
print repr(a)

print 'test b', '-'*20
b = u'你好'
print b
print repr(b)
print b.encode('utf-8')
print repr(b.encode('utf-8'))

输出:

你好 # 以utf-8的表达形式输出
'\xe4\xbd\xa0\xe5\xa5\xbd' # 是 a='你好'的字节码
test b --------------------
你好 # 以utf-8的表达形式输出
u'\u4f60\u597d' # utf-8的编码表现形式
你好 # 变成utf-8的表现形式
'\xe4\xbd\xa0\xe5\xa5\xbd' # 在encode之后，在print输出的是字节码
```
那么如果是以字符串形式展示的utf-8，比如: ```d = "\u4f60\u597d"```. 该如何转化成字节码呢? ```dee = d.decode('raw_unicode_escape');``` 使用这种进行decode.

## 注意的要点
### 格式的统一
对于字符串进行组合的时候要统一格式. 如下例子:

```
a = '你好'
b = u'我很好'

```

虽然在字节码这个层面上是一样的，但是对于字符串来说是不同。a表示的是字节码, ```'\xe4\xbd\xa0\xe5\xa5\xbd'```.而对于b来说是 ```u'\u4f60\u597d'```，所以a,b不能放在一起进行操作。如果要放在一起进行需要将a转成utf-8的形式或者将b转成字节码的形式。

```
a = '你好'
b = u'我很好'

c = a + b.encode('utf-8')
print c, repr(c)

c = unicode(a, 'utf-8') + b
print c, repr(c)

c = a + b
print c

输出:

你好我很好 '\xe4\xbd\xa0\xe5\xa5\xbd\xe6\x88\x91\xe5\xbe\x88\xe5\xa5\xbd'
你好我很好 u'\u4f60\u597d\u6211\u5f88\u597d'
Traceback (most recent call last):
  File "/Users/panxu/Documents/MyProjects/kmeanGame/testUnicde.py", line 49, in <module>
    c = a + b
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe4 in position 0: ordinal not in range(128)
```
如果没有进行转换，就会出现错误。

## Private和Protected的表现方式
```
__abc : 用两个下划线作为前缀是private
_abc: 用一个下划线作为前缀是protected
```
注意：这是是语法层面的私有化，而不是真正意义的私有化，外界还是能破解调用的。不过java也是一样反射依然可以调用。