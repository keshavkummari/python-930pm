#!/usr/bin/python

str1 = "this abc is really a string example....wow!!!"
str2 = "is"

print (str1.rfind(str2))

print (str1.rfind(str2, 0, 10))
print (str1.rfind(str2, 10, 0))

print (str1.find(str2))
print (str1.find(str2, 0, 10))
print (str1.find(str2, 10, 30))


"""
27	rfind(str, beg=0,end=len(string))
	Same as find(), but search backwards in string.
"""
