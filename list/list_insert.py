#!/usr/bin/python

aCoolList = ["superman", "spiderman", 1947,1987,"Spiderman"]

oneMoreList = [22, 34, 56,34, 34, 78, 98]

print (aCoolList)

# inserting values

aCoolList.insert(0, "street750")

print (aCoolList)

print (oneMoreList)

oneMoreList.insert(5,1947)

print (oneMoreList)

'''
3. list.insert(i, x) :
Insert an item at a given position.
The first argument is the index of the element before which to insert,
so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to
a.append(x).
'''
