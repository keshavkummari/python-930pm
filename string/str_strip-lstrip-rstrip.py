#!/usr/bin/python
"""
spyder = "     this is string example....wow!!!     "

print (spyder.lstrip())

spyder_007 = "1212this is string example....wow!!!8888888"

print (spyder_007.lstrip('12'))
print("")
print("**********************************")
spyder_008 = "     Python Django Spyder     "

print ("rstrip",spyder_008.rstrip())
print ("lstrip",spyder_008.lstrip())
print ("strip",spyder_008.strip())

"""
str = "88888888this is string example....wow!!!8888888"
print (str.rstrip('8'))
print (str.lstrip('8'))
print (str.strip('8,!'))

strLower = " this is a lower case string this is a "  # 27 index
print(len(strLower))
print (strLower.strip('this is a '))
print(len(strLower))

"""
strip([chars])
	Performs both lstrip() and rstrip() on string

lstrip()
     Removes all leading whitespace in string.

rstrip()
    Removes all trailing whitespace of string.

"""

