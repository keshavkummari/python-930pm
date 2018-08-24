#!/usr/bin/python

"""
>>> dir(set)
['__and__', '__class__', '__cmp__', '__contains__', '__delattr__', '__doc__', '__eq__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__str__', '__sub__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
"""
# ---------------------- PYTHON SET DATA TYPE ------------------------------- #
"""
# Operations:

1	<		# Comparision Operator
2	<=		# Comparision Operator
3	>		# Comparision Operator
4	>=		# Comparision Operator
5	==		# Comparision Operator
6	!=		# Comparision Operator
7	in					# Membership Operator
8	not in				# Membership Operator
9	is				# Identity Operator
10	is not			# Identity Operator
11	a_set.set							# Methods
12	a_set.union							# Methods
13	a_set.intersection					# Methods
14	a_set.difference					# Methods
15	a_set.symmetric_difference			# Methods
16	a_set.update						# Methods
17	a_set.intersection_update			# Methods
18	a_set.difference_update				# Methods
19	a_set.symmetric_difference_update	# Methods
20	a_set.add							# Methods
21	a_set.remove						# Methods
22	a_set.discard						# Methods
23	a_set.pop							# Methods
24	a_set.issubset						# Methods
25	a_set.issuperset					# Methods
26	a_set.copy							# Methods
27	a_str.join							# Methods
28	len						# Function
29	sum						# Function
30	max						# Function
31	min						# Function
32	zip						# Function
33	sorted					# Function
34	map						# Function
35	filter					# Function
36	reduce					# Function
37	any						# Function
38	all						# Function
39	enumerate				# Function
40	type					# Function
41	isinstance				# Function
42	dir						# Function
43	hasattr					# Function
44	str						# Function
45	repr					# Function

"""
"""
Data Structures: Sets

A set is an unordered collection without duplicates.

When printed, iterated upon, or converted into a sequence,
its elements will appear in an arbitrary, implementation-dependent order.

"""
# --------------------------------------------------------------------------- #
1	Convert Iterable into Set 					=		set()
2	Set Union  									=		a_set.union()
3	Set Intersection   							=		a_set.intersection()
4	Set Difference 								=		a_set.difference()
5	Set Symmetric Difference 					=		a_set.symmetric_difference()
6	Set Union with Mutation  					=		a_set.update()
7	Set Intersection with Mutation 				=		a_set.intersection_update()
8	Set Difference with Mutation 				=		a_set.difference_update()
9	Set Symmetric Difference with Mutation      =		a_set.symmetric_difference_update()
10	Add Element into Set                        =		a_set.add()
11	Remove Specified Element from Set           =		a_set.remove(), a_set.discard()
12	Remove Arbitrary Element from Set           =       a_set.pop()
13	Test for Subset                             =		a_set.issubset()
14	Test for Superset                           =		a_set.issuperset()
15	Copy Set                                    =		a_set.copy()
16	Unsupported Set Operations

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
1	Convert Iterable into Set 					=		set()

# Syntax:
set()
set(an_iter)

# Examples:

print set()
Output : set([])

print (set('abc'))
Output : set(['a' ,'b', 'c'])

print set(['a','b','c','c'])
Output : set(['a', 'c', 'b'])

print set([1, 2, 3, 4, 5, 3, 5])
Output : set([1, 2, 3, 4, 5])

print set((1, 2, 3, 4, 5))
Output : set([1, 2, 3, 4, 5])

print set(set([1, 2, 3, 4]))
Output : set([1, 2, 3, 4])

print set({1: 2, 3: 4})
Output : set([1, 3])

print set(enumerate(['a', 'b', 'c', 'd']))
Output : set([(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')])

NOTE :

Returns a new set with the values from iterable or
iterator an_iter.

If the argument is already a set, it returns a copy, i.e.,
a new set with the same elements.

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
2	Set Union  	=		a_set.union()
# Syntax: a_set.union(an_iter)
# Example:
print (set([1, 2, 3, 4, 5]).union(set([5, 6, 7])))

Output : set([1, 2, 3, 4, 5, 6, 7])

'''Returns the union of set a_set and the set of
elements in iterable an_iter.'''
# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
3	Set Intersection  =	a_set.intersection()

# Syntax: a_set.intersection(an_iter)

# Example:

print(set([1, 2, 3, 4, 5]).intersection(set([5, 6, 7])))
Output : set([5])

'''Returns the intersection of set a_set and the set of elements in iterable an_iter.'''
# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
4	Set Difference =		a_set.difference()

# Syntax: a_set.difference(an_iter)

# Example:

print (set([1, 2, 3, 4, 5]).difference(set([5, 6, 7])))
Output : set([1, 2, 3, 4])

'''Returns a set with all elements from set a_set
that are not in iterable an_iter.'''
# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
5	Set Symmetric Difference =		a_set.symmetric_difference()

# Syntax: a_set.symmetric_difference(anInter)

# Example:

print set([1, 2, 3, 4, 5]).symmetric_difference(set([5, 6, 7]))
Output : set([1, 2, 3, 4, 6, 7])

'''Returns a set with all elements that are in exactly one of set a_set and iterable an_iter.'''
# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
6	Set Union with Mutation =		a_set.update()

# Syntax: a_set.update(an_iter)

# Example:

s = set([1, 2, 3, 4, 5])
s.update(set([5, 6, 7]))

print (s)

Output : set([1, 2, 3, 4, 5, 6, 7])

'''Mutates a_set to be the union of set a_set and the set of elements in iterable an_iter. Returns None.'''

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
7	Set Intersection with Mutation 	=		a_set.intersection_update()

# Syntax: a_set.intersection_update(an_iter)

# Example:

s = set([1, 2, 3, 4, 5])
s.intersection_update(set([5, 6, 7]))

print (s)

Output : set([5])

'''Mutates a_set to be the intersection of set a_set and
the set of elements in iterable an_iter. Returns None.'''
# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
8	Set Difference with Mutation 	=		a_set.difference_update()

# Syntax: a_set.difference_update(an_iter)

# Example:

s = set([1, 2, 3, 4, 5])
s.difference_update(set([5, 6, 7]))
print (s)

Output : set([1, 2, 3, 4])

'''Mutates a_set to be the set difference of set a_set and the
set of elements in iterable an_iter. Returns None.'''
# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
9	Set Symmetric Difference with Mutation      =		a_set.symmetric_difference_update()

# Syntax: a_set.symmetric_difference_update(an_iter)

# Example:

s = set([1, 2, 3, 4, 5])
s.symmetric_difference_update(set([5, 6, 7]))
print (s)

Output : set([1, 2, 3, 4, 6, 7])

'''Mutates a_set to be a set with all elements that are in exactly
one of set a_set and iterable an_iter. Returns None.'''

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
10	Add Element into Set                        =		a_set.add()

# Syntax: a_set.add(x)

# Example:
s = set([1, 2, 3, 4, 5])
s.add(5)

print (s)
Output : set([1, 2, 3, 4, 5])

s.add(6)

print (s)
Output :  set([1, 2, 3, 4, 5, 6])

'''Adds element x to the set a_set. Returns None.'''
# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
11	Remove Specified Element from Set           =		a_set.remove(), a_set.discard()

# Syntax:
a_set.remove(x)
a_set.discard(x)

# Example:

s = set([1, 2, 3, 4, 5])
s.remove(5)
print (s)

s.discard(7)
print (s)

s.discard(3)
print (s)

Output:
set([1, 2, 3, 4])
set([1, 2, 3, 4])
set([1, 2, 4])

'''
Removes element x from set a_set.
If element x is not in a_set, a_set.remove raises an error,
while a_set.discard does not.
Returns None.
'''
# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
12	Remove Arbitrary Element from Set           =       a_set.pop()

# Syntax: a_set.pop()

# Example:

s = set([1, 2, 3, 4, 5])
print s.pop()
print s

Output :
1
set([2, 3, 4, 5])

'''Removes and returns an arbitrary element from set a_set.
Raises an error if there are no elements to remove.'''

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
13	Test for Subset                             =		a_set.issubset()
# Syntax: a_set.issubset(an_iter)
# Examples:

s = set([2, 9, 7, 1])
print s.issubset(s)
Output : True

print (set([2, 9, 7, 1]).issubset(set([1, 7])))
Output : False

print set([2, 9, 7, 1]).issubset(set([1, 2, 3, 4]))
Output : False

print set([2, 9, 7, 1]).issubset(set([1, 2, 3, 4, 5, 6, 7, 8, 9]))
Output : True

print set([2, 9, 7, 1]).issubset([1, 2, 7, 9]
Output : True

'''Returns whether the set a_set is a subset of the set of elements in
 iterable an_iter.'''

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
14	Test for Superset                           =		a_set.issuperset()

# Syntax: a_set.issuperset(an_iter)

# Examples:

s = set([2, 9, 7, 1])
print s.issuperset(s)
Output : True

print set([2, 9, 7, 1]).issuperset(set([1, 7]))
Output : True

print set([2, 9, 7, 1]).issuperset(set([1, 2, 3, 4]))
Output : False

print set([2, 9, 7, 1]).issuperset(set([1, 2, 3, 4, 5, 6, 7, 8, 9]))
Output : False

print set([2, 9, 7, 1]).issuperset([1, 2, 7, 9]
Output : True

'''Returns whether the set a_set is a superset of the set of elements in iterable an_iter.'''
# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
15	Copy Set                                    =		a_set.copy()

# Syntax: a_set.copy()

# Example:

s = set([1, 2, 3, 4, 5])
t = s.copy()

print s == t

print s is t

Output :
True
False

'''Makes a new set with the same elements as a_set.'''
# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
16 . Unsupported Set Operations :

1. |
2. &
3. -
4. ^
5. |
6. =
7. &
8. =
9. -
10. =
11. ^
12. =
13. s.clear()

s = set([1, 2, 3, 4, 5])
t = s.copy()
print (s)

set([1, 2, 3, 4, 5])
print (t)

set([1, 2, 3, 4, 5])
s.clear()

print (s)
set([])

print (t)
set([1, 2, 3, 4, 5])

# --------------------------------------------------------------------------- #
----[Keshav Kummari | Email_id: keshav.kummari@gmail.com  | +91 9908823070 ]-
# --------------------------------------------------------------------------- #
