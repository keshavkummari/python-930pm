#!/usr/bin/python3.6
# set() datatypes

print (set([1, 2, 3, 4, 5]).union(set([2,5,6, 7])))

print(set([1, 2, 3, 4, 5]).intersection(set([5,6, 7])))

print (set([1, 2, 3, 4]).difference(set([5, 6, 7,4])))

print (set([1, 2, 3, 4, 5]).symmetric_difference(set([1,6, 7])))

s = set([1, 2, 3, 4, 5])
print("Calling a Variable : %s" %(s))

s.update(set([1,2,3,4,6, 7]))

print("Updated values : %s" %(s))

s = set([1, 2, 3, 4, 5])
s.intersection_update(set([4,6,7]))
print (s)

s = set([1, 2, 3, 4,5])
s.difference_update(set([5,4,6, 7,3]))
print (s)
