#!/usr/bin/python

str = "Python0007"

print(len(str))

print (str.rjust(20, '*'))

print (str.ljust(25, '#'))

"""
29	rjust(width,[, fillchar])
	Returns a space-padded string with the original
	string right-justified to a total of width columns.
"""
#!/usr/bin/python

"""2. center() Method:

Note: 
Returns centered in a string of length width. 
Padding is done using the specified fillchar. Default filler is a space.

Syntax : str.center(width[, fillchar])

width -- This is the total width of the string.
fillchar -- This is the filler character."""

abc_string_1 = "abcdef"

abc_string = """abcd \
tools \
py  \
"""

print ("abc_string.center(10, 'K') : ", abc_string_1.center(11, '&'))
print("")
print ("abc_string.center(10, 'J') : ", abc_string.center(30, 'J'))





