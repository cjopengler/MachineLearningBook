# coding:utf-8

from sys import argv
from string import replace, find, lower
import os
from os import makedirs, unlink, sep
from os.path import isdir, exists, dirname, splitext
from htmllib import HTMLParser
from urllib import urlretrieve
from urlparse import urlparse, urljoin
from formatter import DumbWriter, AbstractFormatter
from cStringIO import StringIO

class Retriever(object): #下载网页
    def __init__(self, url):
        # 网页url
        self.url = url
        # 用url创建本地文件,用来保存下载的文件
        self.file = self.filename(url)

    def filename(self, url, deffile='index.htm'): # 创建本地文件
        parseurl = urlparse(url, 'http:', False)
        path = parseurl[1] + parseurl[2]

        if parseurl[2] == '':
            path += '/' + deffile

        ext = splitext(path)

        if ext[1] == '':
            if path[-1] == '/':
                path += deffile
            else:
                path += '/' + deffile

        ldir = dirname(path)

        if sep != '/':
            ldir = replace(ldir, ',', sep)

        # ldir = ('''%s/%s''' % (os.getcwd(), ldir))

        if not isdir(ldir):
            if exists(ldir):unlink(ldir)
            try :
                makedirs(ldir)

            except Exception, e:
                print e

        return path

    def download(self): # 下载网页
        try:
            retval = urlretrieve(self.url, self.file)

        except IOError, e:
            retval = ('***Error:%s, invalid URL "%s"' % (e, self.url))

        return retval

    def parseAndGetLinks(self): #拆分 HTML, 保存连接
        self.parser = HTMLParser(AbstractFormatter(DumbWriter(StringIO())))
        self.parser.feed(open(self.file).read())
        self.parser.close()
        return self.parser.anchorlist





class Crawler(object):
    count = 0

    def __init__(self, url):
        # 需要爬的url地址
        self.q = [url]
        # 已经爬过的放在 seen里
        self.seen = []
        # dom 站点
        self.dom = urlparse(url)[1]

    def getPage(self, url):
        r = Retriever(url)
        retval = r.download()

        if retval[0] == '*':
            print retval, '... skipping parse'
            return

        Crawler.count = Crawler.count + 1

        print '\n(', Crawler.count, ')'
        print 'URL:', url
        print 'FILE:', retval[0]
        self.seen.append(url)

        links = r.parseAndGetLinks()

        for eachlink in links:
            if eachlink[:4] != 'http' and find(eachlink, '://') == -1:
                eachlink = urljoin(url, eachlink)

            print '*', eachlink

            # 去掉邮件地址
            if find(lower(eachlink), 'mailto:') != -1:
                print '...丢弃邮件地址'
                continue

            if eachlink not in self.seen:
                if find(eachlink, self.dom) == -1:
                    print '...丢弃,不在域中'
                else:
                    if eachlink not in self.q:
                        self.q.append(eachlink)
                        print '%s add to Q' % eachlink

                    else:
                        print '%s has in Q' % eachlink
            else:
                print '%s has been processed'

    def go(self):
        while self.q:
            url = self.q.pop()
            self.getPage(url)

            if (Crawler.count > 9):
                break


def main():

    if len(argv) > 1:
        url = argv[1]
    else:
        url = '''http://www.csdn.net''';
        # url = '''http://www.csdn.net/company/statement.html'''

    if not url: return

    robot = Crawler(url)
    robot.go()

if __name__ == '__main__':
    main()