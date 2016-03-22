# Chapter12 模块
## 模块的路径搜索
PYTHONPATH 这个环境变量中定义了python的模块路径。也可以在程序中导入，使用sys.path.append('/home/wesc/py/lib') 来进行导入.

## 缩短导入
```
import Tkinter as tkfrom cgi import FieldStorage as form
```
使用 ```as```关键字。
