#!/usr/bin/python
'''
modes to open file :
r, rb, r+, rb+, w, wb, w+, wb+, a, ab, a+, ab+
'''
#Writing a file

fileObject = open("sample.txt","r+t")
fileObject.write("Python OS Module SYS Module")
fileObject.close()

#Reading a file

fileObjectNew = open("sample.txt", "r+")
fileText = fileObjectNew.read(200)
print ("fileText",fileText)
fileObjectNew.close()


