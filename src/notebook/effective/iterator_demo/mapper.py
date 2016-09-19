#!/bin/python
# coding: utf-8

import sys


def read_input(f):
    for l in f:
        yield l.strip().split()


def main():
    # if len(sys.argv) < 2:
    #     print 'usage:python mapper.py config_file'
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            print '%s%s%d' % (word, '\t', 1)


def test():
    pass


if __name__ == '__main__':
    # test()
    main()
