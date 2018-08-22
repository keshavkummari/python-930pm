#!/usr/bin/python

fileName = {'Course':'Python','course':'Perl','type' : 'Video', 'boolean': 1 }

sample = {1: "one", 2 : "two"}

print(fileName)
print (fileName.get('type'))

#print (fileName.has_key('Video'))
print (fileName.items())

#reset the dictionary
# print (sample.clear())
# print (sample)

#getting all key and values
print ("Calling All Keys : ",fileName.keys())
print ("Calling All Values : ",fileName.values())
