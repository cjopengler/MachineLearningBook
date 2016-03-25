# coding:utf-8
from HTMLParser import HTMLParser
from urlparse import urlparse, urljoin

import os

help(os.path.isdir)

try:
    print os.getcwd()
    print os.path.abspath(os.curdir)
    print os.path.abspath('.')

    print os.path.isdir('www.csdn.net/company')
    print os.path.isdir('abc/d')
    os.makedirs('www.csdn.net/company')
except Exception, e:
    print e