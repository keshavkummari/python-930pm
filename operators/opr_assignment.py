#!/usr/bin/python3
a = 21
b = 10
c = 0

c = a + b
print ("Line 1 - Value of c is ", id(a),id(b),id(c),type(c),c)

print(c)
c += a
print ("Line 2 - Value of c is ", id(a),id(b),id(c),type(c),"c + a", c , sep=':')

print(c)
c *= a
print ("Line 3 - Value of c is ", id(a),id(b),id(c),type(c),c )

print(c)
c /= a
print ("Line 4 - Value of c is ", id(a),id(b),id(c),type(c),c )

c = 2
print(c)
c %= a
print ("Line 5 - Value of c is ", id(a),id(b),id(c),type(c),c)

print(c)
c **= a
print ("Line 6 - Value of c is ", id(a),id(b),id(c),type(c),c)

print(c)
c //= a
print ("Line 7 - Value of c is ", id(a),id(b),id(c),type(c),c)
