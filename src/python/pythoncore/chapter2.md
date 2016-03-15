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

## 下面是测试代码
```
import sys

# print >> sys.stderr, 'Fatal error: invalidate pinut'

logfile = open('./log.txt', 'a')
print >> logfile, 'Fatal Error: invalid input'

logfile.close()

# num = raw_input('Now enter a number: ')
# print 'Double your number: %d' % (int(num) * 2)

# help(raw_input)
n = 3
print --n

alist = [1, 2, 3, 4]
print alist[2:]
print alist[3]

aTuple = ('name', 1, 2, 'year')
print aTuple
print aTuple[:3]

aDict = {'host': 'earth', 'port':80}
print aDict

print aDict['host']

for key in aDict:
    print key, aDict[key]

a = 2

if a == 2:
    print 'a is 2'

elif a < 2:
    print 'a less 2'

else:
    print 'a > 2'

while a > 0:
    print 'a is %d' % a
    a -= 1

for num in [1, 2 ,3]:
    print num,

print '\n'

print range(1, 9, 2)
print range(4)

foo = 'abc'

for i, ch in enumerate(foo):
    print ch, '%d' % i,

print '\n'

squared = [x**2 for x in range(4)]

print squared

sqdEvens = [x**2 for x in range(4) if not x%2]
print sqdEvens

# fobj = open('log.txt')
#
# for eachline in fobj:
#     print eachline,
#
# fobj.close()

def addMe2Me(x=2):
    'apply + operation to argument'
    return (x+x)

x = addMe2Me()

print x

class FooClass(object):
    'my very first class: foo class'
    version = 0.1
    def __init__(self, nm = 'John'):
        'constructor'
        self.name = nm
        print 'Create a class instatns for', nm

    def showname(self):
        'display instance attribute and class name'
        print 'Your name is', self.name
        print 'm=My name is', self.__class__.__name__

    def showver(self):
        'display class attribute'
        print self.version

foo1 = FooClass()

foo1.showname()

print dir(sys)

输出:
Python is number 1
abcabcabc
3
[3, 4]
4
('name', 1, 2, 'year')
('name', 1, 2)
{'host': 'earth', 'port': 80}
earth
host earth
port 80
a is 2
a is 2
a is 1
1 2 3 

[1, 3, 5, 7]
[0, 1, 2, 3]
a 0 b 1 c 2 

[0, 1, 4, 9]
[0, 4]
4
Create a class instatns for John
Your name is John
m=My name is FooClass
['__displayhook__', '__doc__', '__egginsert', '__excepthook__', '__name__', '__package__', '__plen', '__stderr__', '__stdin__', '__stdout__', '_clear_type_cache', '_current_frames', '_getframe', '_mercurial', 'api_version', 'argv', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_clear', 'exc_info', 'exc_type', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'gettrace', 'hexversion', 'long_info', 'maxint', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'py3kwarning', 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit', 'settrace', 'stderr', 'stdin', 'stdout', 'subversion', 'version', 'version_info', 'warnoptions']


```

