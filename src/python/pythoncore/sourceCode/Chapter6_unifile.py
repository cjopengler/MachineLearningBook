#!/usr/bin/env python
# coding:utf-8

CODEC = 'utf-8'
FILE = 'unicode.txt'

hello_out = '你好 hello\n'





f = open(FILE, 'w')
f.write(hello_out)
f.write('我很好\n')
f.close()

f = open(FILE, 'r')
bytes_in = f.read()

print bytes_in
f.close()

hello_in = bytes_in.decode(CODEC)

print hello_in