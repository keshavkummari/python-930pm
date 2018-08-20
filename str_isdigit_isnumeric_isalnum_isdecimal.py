#!/usr/bin/python
"""
str1 = "123abc"  # No space in this string
#print (str1.isalnum())
str2 = "Python world....wow!!!"
#print (str2.isalnum())

a='10'
b="ab"

print(a.isalnum())
print(b.isalnum())

# Below is the example of isdigit() method:
print(a.isdigit())   # True
print(b.isdigit())   # Flase
print(str1.isdigit()) # False 
print(str2.isdigit()) # False



10	isalnum()
	Returns true if string has at least 1 character and all
	characters are alphanumeric and	false otherwise.

12	isdigit()
	Returns true if string contains only digits and false otherwise.


print("isdigit")
str = "2020"  # No space in this string
print (str.isdigit())

str = "Python world....wow!!!";
print (str.isdigit())

12	isdigit()
	Returns true if string contains only digits and false otherwise.

"""	


print("isnumeric")

_007 = u"$6"
print (_007.isnumeric())

_008 = u"786786"
print (_008.isnumeric())

_008 = "786786"
print (_008.isnumeric())

_009 = "#03948274"  # Only digit in this string
print (_009.isdigit())

_006 = "Linux Unix Perl Python and django...etc!!! 0009"
print (_006.isdigit())


"""
14	isnumeric()
	Returns true if a unicode string contains only numeric
	characters and false otherwise.
"""


#!/usr/bin/python
"""
str1 = "44"
print (str1.isdecimal())

str2 = u"695979"
print (str2.isdecimal())
"""
#c = "\u0123456789" # decimal-radix numbers
#c = '\u2155'
#c = '\u214675'
#c = r'\u2155'
#c = u"77"
#c = "77"
c = u'77'  # 0-9

print(c)
print(c.isdecimal())
print(c.isdigit())
print(c.isnumeric())

print(c.isdecimal(), c.isdigit(), c.isnumeric())

