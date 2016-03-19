# Chapter10 错误和异常

```
# coding: utf-8

## 异常处理

def safe_float(obj):
    'safe version of float()'
    try:
        retval = float(obj)
    except (ValueError, TypeError), diag:
        retval = str(diag)
    else:
        print '没有任何错误'
    finally:
        print '最后还是要执行'

    return retval

print safe_float(11)

# raise 似乎与throw是一样的? sys.exc_info()可以获得异常信息
try:
    assert 1==2
except AssertionError:
    import  sys
    exc_tuple = sys.exc_info()
    print exc_tuple


输出:
/System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7 /Users/panxu/PycharmProjects/PythonCore/Chapter10.py
没有任何错误
最后还是要执行
11.0
(<type 'exceptions.AssertionError'>, AssertionError(), <traceback object at 0x10b24b878>)

Process finished with exit code 0

```