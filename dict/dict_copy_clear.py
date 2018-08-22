#!/usr/bin/python
"""
ronnie = {'Name': 'minnu', 'Age': 7}

print("Student name is {0} and his age is {1}" .format(ronnie['Name'],ronnie['Age']))
print("Student name is {0} and his age is {1}" .format("Naresh",7))
print ("Length : %d" % len(ronnie)) # len() is function
print("FirstName: %s MiddleName: %s LastName: %s Age: %d" %('Guido','Van','Rossum',58))

dict_1 = {'Name':'minnu','Age':7}
print ("Equivalent String : %s" % str(dict_1))  # str() is function

dict_2 = {'Name': 'minnu', 'Age': 7}
print ("Variable Type : %s" % type(dict_2)) # type() is function

dict_3 = {'Name': 'minnu', 'Age': 7};

print ("Start Len : %d" % len(dict_3))
"""
dict={"FirstName":'Guido',"MiddleName":'Van',"LastName":'Rossum','Age':58}

print(dict)

#dict.clear()   # clear() is method

print ("End Len : %d" %  len(dict))

print(dict,type(dict),id(dict))

dict_5 = dict.copy() # copy() is method

print ("New dictinary : %s" % str(dict_5))
