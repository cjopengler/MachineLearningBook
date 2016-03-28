# Chapter11 函数和函数式编程
python支持内嵌函数，也就是一个函数内部可以再声明一个函数。因为函数本身来说，就是类。

## 函数的装饰者
这就是装饰者模式。装饰者，在数学的表达很优雅 ```g(f(x))```就是这种表达式。

关于装饰者的详解。在Java的装饰者模式，我们清楚是对一个接口的装饰。这和函数的装饰本质上是一样的。那么，在Java的装饰者模式中，是如何进行处理的呢？

1 需要传递一个接口对象，作为装饰类的参数
2 调用接口的时候，会先执行装饰的接口调用，再次执行真正本身的调用。

那么，上面的步骤在函数的装饰者中是如何执行?

### 无参函数装饰

```
print '... dec'
def dec():
    def wraper(f):
        print 'dec is called'
        return f

    return wraper

@dec()
def f():
    print 'f is called'

f()
```

逐条进行分析。

1 需要传递一个接口对象，作为装饰类的参数。这里的解释是，dec()中没有参数，那么 f 会作为参数传递给dec()中的第一个内部函数，也就是 wraper的参数。

2 执行。执行的时候，先执行 dec()->wraper->f 注意，最后返回的是f函数，也就是说经过装饰之后，最后返回的是f

### 有参数的装饰者
在这里必须搞清楚一点，就是在装饰者模式中，因为不论是装饰者还是被装饰者都是继承自同一个接口，所以，二者的接口是一样的，也就是参数是一样的。而在python的函数装饰中，可能就会产生不一样的参数。

```
def decarg(a, b):
    print 'decarg is called', a, b

    def wraper(func):
        def test(a, b):
            print 'test is called', a, b
            return func()

        return test

    return wraper

@decarg('a', 'b')
def farg():
    print 'farg is called'
    return 3

print farg('a', 'b')

输出:
... decarg
decarg is called a b
test is called a b
farg is called
3
```

继续逐个分析:

1 参数传递。这里显然 func就是 frag 函数。
2 执行。注意这里的，decagr和farg的参数是不一样的。那么如何来处理这个问题呢？增加了一个新的内部函数test.所以这里的调用顺序是这样的: decarg->wraper -> test ->func

这里看起来还有一点疑惑的地方，是什么呢？是不是感觉和无参的对比多了一层test? 如果去掉test，直接返回func呢？会得到一个错误。所以关于有参数的装饰器来说，farg('a', 'b')的参数 ('a','b')究竟传给了谁？ 是 wraper函数的返回值。所以对于装饰器来说的真的执行顺序是这样的:

decarg => Run => return wraper => frag作为参数传递给wraper => wraper run => return test => ('a','b')作为参数传递给test => test run => frag Run=> return frag的执行结果

如果和类对比，到很有意思。 decarg类似于最外层的类，waper是接口的实现，执行完wraper，执行func. 而test是一个适配器，为了解决参数不一致的适配器，最终执行func.

注意:@decarg('a', 'b') 这里的'a','b'表示传递给decarg函数的，不是形参。


## 生成器
生成器函数和函数长成一个样子，难道是靠内部有yield来标识这是一个生成器吗?

```
def simpleGen():
    yield  1
    yield '2-->punch'

myG = simpleGen()
print myG.next()
print myG.next()

for eachItem in simpleGen():
    print eachItem
    
输出:
1
2-->punch
1
2-->punch

```

生成器的最大的威力在于进行“协同程序”作战。 yield 将当前程序挂起，然后去执行其他的程序，执行完其他程序再继续执行当前程序。可以进行多线程和多进程的程序的协同工作。

通过对生成器传递参数也可以。

```
count = counter(5)
print count.next(), count.next()

count.send(9)

print count.next()
count.close()

输出:
5 6
10
```