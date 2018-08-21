#!/usr/bin/python


tuple1, tuple2 = ('abc', 'xyz', 'minnu', 'ABC'), (456, 700, 200)

print ("Min value element : ", min(tuple1))
print ("Max value element : ", max(tuple1))
print("")
print ("Min value element : ", min(tuple2))
print ("Max value element : ", max(tuple2))

aList = ['123', 'xyz', 'minnu', 'abc']
aTuple = tuple(aList) # Converting the list to tuple using tuple() function

print ("Tuple elements : ",min(aTuple),max(aTuple),type(aTuple),id(aTuple),aTuple)

aTuple = (123, 'xyz', 'minnu', 'abc')
aList = list(aTuple)
print ("Tuple elements : ",type(aList) ,aList)
