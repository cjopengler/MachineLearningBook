from __future__ import  division
a = 1/2
b = 1 // 2
c = 1.0 / 2.0
d = 1.0 // 2.0
e = -1 // 2
f = -1 / 2

g = 5 % 2
print a, b, c, d, e, f, g


m = coerce(1.1, 11L)

print abs(-1), coerce(1.3, 134L), m[1], divmod(10, 3), pow(2, 5),round(3.45, 2)

from decimal import  Decimal
dec = Decimal('.1')

print dec, dec + Decimal('1.0')