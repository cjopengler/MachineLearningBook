#!/bin/python
# coding: utf-8

from itertools import groupby
from operator import itemgetter
import sys


def read_mapper_output(f, sep='\t'):
    for l in f:
        yield l.rstrip().split(sep, 1)


def main(sep='\t'):
    data = read_mapper_output(sys.stdin, sep=sep)
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            print '%s%s%d' % (current_word, sep, total_count)
        except ValueError:
            pass


if __name__ == '__main__':
    main()
