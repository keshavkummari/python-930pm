#!/usr/bin/python

x = float(input("1st Number: "))
y = float(input("2nd Number: "))
z = float(input("3rd Number: "))

if x < y:
    if x < z:
        minimum = x
    else:
        minimum = z
else: 
    if y < z:
        minimum = y
    else:
        minimum = z

print("The minimum value is: " ,
      str(minimum))
