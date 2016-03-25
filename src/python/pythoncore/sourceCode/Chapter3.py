a = 3 \
    + 2
print a

(x, y, z) = (1, 2, 'abc')

print "x=%d, y=%d, z=%s" % (x, y, z)

(x, y) = (y, x)

print "x=%d, y=%d, z=%s" % (x, y, z)

#!/usr/bin/env python

'makeTextFile.py -- create text file'

import os
ls = os.linesep

# get filename
while True:

    fname = raw_input("Input a file name:")
    
    if os.path.exists(fname):
        print"*** ERROR: '%s' already exists" % fname
    else:
        break

# get file content (text) lines
all = []
print "\nEnter lines ('.' by itself to quit).\n"

# loop until user terminates input
while True:
    entry = raw_input('> ')
    if entry == '.':
        break
    else:
        all.append(entry)

# write lines to file with proper line-ending
fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print 'DONE!'
