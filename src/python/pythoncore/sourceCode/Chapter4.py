print type(42)

a = None
print a

foostr = 'abcdef'

print foostr[::-1]

x = [1, 2, 3, 4]
y = x
z = [1, 2, 3, 4]

print x is y
print x is z
print x is not y

print type([])

def displayNumType(num):
    print num, 'is',

    if isinstance(num, (int, long, float, complex)):
        print 'a number of type:', type(num).__name__
    else:
        print 'not a number at all'

displayNumType(-69)