#!/usr/bin/python

'''Identity operators in Python:
1. is 
2. is not'''

score = 10
player = 11

print (id(score))
print (id(player))
     
if (score is player):
    #print ("Yes we are not the same")
    print ("Yes we are same")
else:
    print ("We are not same")
    
 
