#!/usr/bin/python
"""
18	join(seq)
	Merges (concatenates) the string representations of elements in sequence seq into a string,
	with separator string.
"""	
s = "  &  "
seq = ("a", "b", "c") # This is sequence of strings.

print("Calling A Variable i.e. ",s, id(s),type(s),len(s))
print("")
print("Calling A Variable i.e. ",seq, id(seq),type(seq),len(seq))

print (s.join(seq))


joiner = "-"
title="10 20 30 Abc"

#title = "my first blog post"
#title = ("my", "first", "blog", "post")
strLower = "abc"

print(title)

print (joiner.join(title))


