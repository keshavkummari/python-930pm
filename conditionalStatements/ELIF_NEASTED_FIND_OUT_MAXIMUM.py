#!/usr/bin/python

x = float(input("1st Number: "))  5
y = float(input("2nd Number: "))  4
z = float(input("3rd Number: "))  6

if x > y:
    if x > z:
        maximum = x
    else:
        maximum = z
else: 
    if y > z:
        maximum = y
    else:
        maximum = z

print("The maximam value is: "+ str(maximum))
