# 环境搭建
[官方网址](https://www.tensorflow.org/)

mac安装使用的是pip，具体命令参考 [pip安装](https://www.tensorflow.org/versions/r0.8/get_started/os_setup.html#pip-installation)

## 安装问题列表

## 1 C compiler cannot create executables
当安装程序的时候，有的时候会出现这个错误。
### 解决方案
是因为 “Command Line Tools“ 没有安装。安装的方法如下:

[Command Line Tools 安装](http://www.07net01.com/2015/07/879465.html)

## 2 Operation not permitted
当mac升级到最新的时候，通过脚本安装程序的时候因为可能会修改系统文件夹。那么就会出现这个错误，即使管理员权限也不行。这是苹果的保护机制，只有苹果的签名程序可以操作。

[知乎解决方案1](https://www.zhihu.com/question/36108835/answer/65969780)

[国外解决方案2](https://www.quora.com/How-do-I-turn-off-the-rootless-in-OS-X-El-Capitan-10-11)

## 3 ImportError: numpy.core.multiarray failed to import
这是因为在安装Tensorflow的时候会下载，numpy到对应的版本。而MAC本身也带了numpy，而mac自身的numpy版本较低导致的。办法就是，删除mac自带的numpy即可。使用tensorflow 下载的。

第一步确定系统的numpy安装路径:

```
mport numpy as np
np.path

输出结果:
['/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/numpy']

删除该系统目录下的numpy:
sudo rm -rf /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/numpy
```

## 4 ImportError: No module named protobuf

这是因为 protobuf的版本比较旧了。最简单的办法是删除 protobuf，在重新安装 tensorflow即可。

```
sudo pip uninstall protobuf
sudo pip uninstall tensorflow
```


