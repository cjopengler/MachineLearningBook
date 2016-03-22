# Chapter11 函数和函数式编程
python支持内嵌函数，也就是一个函数内部可以再声明一个函数。因为函数本身来说，就是类。

## 函数的装饰者
这就是装饰者模式。装饰者，在数学的表达很优雅 ```g(f(x))```就是这种表达式。

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