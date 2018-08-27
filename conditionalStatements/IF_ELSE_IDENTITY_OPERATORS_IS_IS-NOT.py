#!/usr/bin/python

score = 10
player = 10

print (id(score))
print (id(player))

if (score is player):
    print ("Yes they are the same")
else:
    print ("We are not same")
    
#Alternative to is

if (id(player) == id(score)):
    print ("Alternative to is and not is")
