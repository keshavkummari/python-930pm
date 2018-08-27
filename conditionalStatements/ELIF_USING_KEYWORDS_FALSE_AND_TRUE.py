#!/usr/bin/python
# True or False (Keywords)
balance = 100

if balance > 200:   # False
    print ("This is block 1")
    print ("THis is block 1 part 1")
#elif True:                              # Keywords [i.e. True|False]
elif balance >= 200:  # False
    print ("This is block 2")
elif balance == 200:   # False
    print ("This is block 3")
#elif balance == 200:
elif True:
    print("4th Elif")
else:
    print ("This is final else")
   
# one more Method
highScore = 100

if (highScore == 100): print ("Some high score broken!")

#elif True:
#elif False:
