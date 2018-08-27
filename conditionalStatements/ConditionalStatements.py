*************************************************************************************
1. The 1. if  2. if..else , 3. elif  and 4. neasted elif

1. IF Statement:

my_var=50
    #50 < 100:
if my_var<100:
    print (my_var is less then 100)
print ("We are out of the if statement")

#The if statement is used for conditional execution:

#if_stmt ::=  "if" expression ":" suite

#(or)

my_var=50

if my_var<100:
    print ("Yes")
    print ("my_var is less then 100")
print ("We are out of the if statement")

*************************************************************************************
2. IF..ELSE STATEMENT : 

var_1=50
if var_1>100:
    print (var_1, "is less than 100")
else:
    print ("var_1 is not less than 100")
	
print ("We are out of the if..else block")

*************************************************************************************
3. ELIF STATEMENT : 

perl=50
python=80

if (perl>python):
    print ("Perl Course fee is more than python fee")
elif(perl==python):
    print ("Perl course fee is less than python fee")
elif(perl<python):
    print ("Perl course fee is equal to python fee")
elif(perl!=python):
    print ("Perl course fee is not less than python fee")
else:
    print ("None of the above are matched")
    
print ("We are out of the if..elif block") 

*************************************************************************************
3. NESTED IF-ELSE STATEMENT : 

>>> ord('A')
65
>>> ord("Z")
90
>>> ord('a')
97
>>> ord("z")
122


char=input("Please enter any charcter : ")
if ord(char)>=65 and ord(char)<=90:
    print ("You entered an upper case alphabet")
    if char in ['A','E','I','O','U']:
        print ("You entered A vowel.",char)
    else:
        print ("You entered a consonant.", char)
elif ord(char)>=97 and ord(char)<=122:
    print ("You entered a vowel.")
    if char in ['a','e','i','o','u']:
        print ("You entered a vowel.")
    else:
        print ("You entered a consonant.")
else:
    print ("You did not enter an alphabet.")
print ("We are out of the if..elif block")
*************************************************************************************
Identity operators in Python:
1. is 
2. is not
Membership operators:
1. in 
2. not in
*************************************************************************************
Using keyword : False:

#!/usr/bin/python
balance = 100

if balance > 200:
    print ("This is block 1")
    print ("THis is block 1 part 1")
elif False:
    print ("This is block 2")
elif False:
    print ("This is block 3")
    
else:
    print ("This is final else")
   
# one more Method
highScore = 100

if (highScore == 100): print ("Some high score broken!")
*************************************************************************************
Membership operators:
1. in 
2. not in

#!/usr/bin/python

score = 10
mark = 4

milestone = [1, 2, 3, 4, 5, 6, 7, 8]

if (score not in milestone):
    print ("You reached the milestone")
else:
    print ("No milestone so far")
*************************************************************************************
Identity operators in Python:
1. is 
2. is not

#!/usr/bin/python

score = 10
player = 10

print (id(score))
print (id(player))

if (score is not player):
    print ("Yes they are the same")
else:
    print ("We are not same")
    
#Alternative to is

if (id(player) == id(score)):
    print ("Alternative to is and not is")


var = 10

print (id(var))
*************************************************************************************
Using input method:

#!/usr/bin/python

star = int(input("Please give us rating between 1 and 5\n"))

if star <= 0 or star >= 6:
    print ("Please enter a valid number\n")
    exit()
    
if star == 1:
    print ("Your rating was 1")
elif star == 2:
    print ("Your rating was 2")
elif star == 3:
    print ("Your rating was 3")
elif star == 4:
    print ("Your rating was 4")
else:
    print ("Your rating was", star)
*************************************************************************************
