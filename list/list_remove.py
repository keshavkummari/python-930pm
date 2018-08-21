#!/usr/bin/python

aCoolList = ["superman", "spiderman", 1947,1987,1947,"Spiderman"]

oneMoreList = [22, 34, 56,34, 34, 78, 98]

print (aCoolList)

aCoolList.remove('Spiderman')
print (aCoolList)

aCoolList.remove(2017)
print (aCoolList)

# deleting values
aCoolList.pop(1)  # With specific index
print(aCoolList)

aCoolList.pop()   # Last element from the list
print (aCoolList)

"""
4. list.remove(x) :
Remove the first item from the list whose value is x.
It is an error if there is no such item.
"""
