#!/usr/bin/python

"""
26	replace(old, new [, max])
	Replaces all occurrences of old in string with new or at
	most max occurrences if max given.
"""

str = "python is scripting is and is programming is language"

print (str.replace("is", "was"))
print("")
print (str.replace("is", "was", 3))
