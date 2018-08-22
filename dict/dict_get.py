#!/usr/bin/python

studnet = {'Name': 'Minnu', 'Age': 7}  # Dict Variable

print ("Value :",studnet.get('Age'))

print ("Value :",studnet.get(7)) # We can not call a value

print ("Value : %s" % studnet.get('Age'))

print ("Value : %s" %  studnet.get('Education', "Python"))

fileName = {'Course':'Python', 'type' : 'Video', 'boolean': 1 }

sample = {1: "one", 2 : "two"}

print (fileName.get('type'))
