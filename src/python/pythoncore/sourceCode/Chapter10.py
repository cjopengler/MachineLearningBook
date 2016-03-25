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


