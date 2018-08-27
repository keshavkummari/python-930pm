********************************************************************
# Python Decision Making using Control Flow or Conditional Statements in Python:

'''
Decision making is anticipation of conditions occurring while execution of the program and 
specifying actions taken according to the conditions.

Decision structures evaluate multiple expressions which produce TRUE or FALSE as outcome.

You need to determine which action to take and which statements to execute if outcome is TRUE or FALSE otherwise.
'''

1. The if statement :

The if statement is used for conditional execution:

if_stmt ::=  "if" expression ":" suite
             ( "elif" expression ":" suite )*
             ["else" ":" suite]
			 
********************************************************************
# Examples: Simple If condition :

#!/usr/bin/python
course_name="Python"
if course_name:		# suite : 
   print "1 - Got a true expression value"
   print "Course Name: Python"
   print "Course Duration: 30-Hours"
   print "Daily 1 Hr"
   print course_name

********************************************************************
#!/usr/bin/python
value_2 = 2
if value_2:  	   # suite : 
   print "2 - Got a true expression value"
   print value_2
print "We are out of Simple If condition"
********************************************************************
#!/usr/bin/python
var = 100
if ( var == 100 ): print "Value of expression is 100"
print "Good bye!"			 

#or 

var = 100
if ( var == 100 ):  # suite : 
    print "Value of expression is 100" # 4 whitespacess or one tab 
print "Good bye!"

# or 

var = 100
if var == 100:      # suite : 
        print "Value of expression is 100" # 4 whitespacess or one tab 
print "Good bye!"

# or

var = 100
if var == 100: print "Value of expression is 100" # 4 whitespacess or one tab
print "Good bye!"

#or 

var = 100
if [ var == 100 ]:     # suite : 
    print "Value of expression is 100"  # 4 whitespacess or one tab 
print "Good bye!"

#or 

var = 100
if [ var == 100 ]: print "Value of expression is 100"  # 4 whitespacess or one tab 
print "Good bye!"

*********************************
#!/usr/bin/python

course = "python"
course_1 = 'python'

if ( course == course_1 ) : print "Got a true expression value"
print "Good bye!"

# or

course = "python"
course_1 = 'python'
if course == course_1:
        print "Got a true expression value"
print "Good bye!"
********************************************************************
Python IF...ELIF...ELSE Statement :

'''
An else statement can be combined with an if statement. 
An else statement contains the block of code that executes if the conditional expression 
in the if statement resolves to 0 or a FALSE value.

The else statement is an optional statement and there could be 
at most only one else statement following if .
'''

Syntax :

if expression:
   statement(s)
else:
   statement(s)

#!/usr/bin/python

a_1 = 100

if a_1 == 200:
   print "1 - True expression value"
   print a_1
else:
   print "1 - False expression value"
   print a_1

var = 50   
if ( var != 100 ) : print "Value of expression is 100"
else: print "Value of var is not 100"
print "Good bye!"

course = "python"
course_1 = 'python'

if [ course == course_2 ]:
    print "Got a true expression value"
else:
    print "Got a false expression value"
print "Good bye!"

# or 

if course == course_2:
    print "Got a true expression value"
else:
    print "It's false expression"

********************************************************************
"""Note:
A compound statement consists of one or more ‘clauses.’ 
A clause consists of a header and a ‘suite.’ 
The clause headers of a particular compound statement are all at the same indentation level. 
Each clause header begins with a uniquely identifying keyword and ends with a colon. 
A suite is a group of statements controlled by a clause. 
A suite can be one or more "semicolon-separated" simple statements on the same line as the header, 
following the header’s colon, or it can be one or more indented statements on subsequent lines."""
********************************************************************

3. The elif Statement :

The elif statement allows you to check multiple expressions for TRUE 
and execute a block of code as soon as one of the conditions evaluates to TRUE.

Syntax:

if expression1:
   statement(s)
elif expression2:
   statement(s)
elif expression3:
   statement(s)
else:
   statement(s)
********************************************************************
#!/usr/bin/python

fee_1 = 10
if fee_1 == 20:
   print("1 - Got a true expression value")
   print(fee_1)
elif fee_1 == 10:
   print("2 - Got a true expression value")
   print(fee_1)
elif fee_1 == 10:
   print("3 - Got a true expression value")
   print(fee_1)
else:
   print "4 - Got a false expression value"
   print fee_1

print "Good bye!"

*********************************
#!/usr/bin/python

number = 23
guess = int(input('Enter an integer : '))

if guess == number:
    # New block starts here
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # New block ends here
elif guess < number:
    # Another block
    print('No, it is a little higher than that')
    # You can do whatever you want in a block ...
else:
    print('No, it is a little lower than that')
    # you must have guessed > number to reach here

print('Done')
# This last statement is always executed,
# after the if statement is executed.

********************************************************************

4. Python nested IF statements : 

'''
When you want to check for another condition after a condition resolves to true. 

In such a situation, you can use the nested if construct.

In a nested if construct, you can have an "if...elif...else" construct inside another if...elif...else construct.
'''

Syntax:

The syntax of the nested if...elif...else construct:

if expression1:
   statement(s)
   if expression2:
      statement(s)
   elif expression3:
      statement(s)
   else:
      statement(s)
elif expression4:
   statement(s)
else:
   statement(s)
********************************************************************

#!/usr/bin/python

mac_os = 100
if mac_os < 200:
   print "Expression value is less than 200"
   if mac_os == 150:
      print "Which is 150"
   elif mac_os == 100:
      print "Which is 100"
   elif mac_os == 50:
      print "Which is 50"
elif mac_os < 50:
   print "Expression value is less than 50"
else:
   print "Could not find true expression"

print "Good bye!"
********************************************************************
Find out the maximum value: 

#!/usr/bin/python

x = float(input("1st Number: "))
y = float(input("2nd Number: "))
z = float(input("3rd Number: "))

if x > y:
    if x > z:
        maximum = x
    else:
        maximum = z
else: 
    if y > z:
        maximum = y
    else:
        maximum = z

print("The maximam value is: " + str(maximum))
********************************************************************
Find out the minimum value: 

#!/usr/bin/python

x = float(input("1st Number: "))
y = float(input("2nd Number: "))
z = float(input("3rd Number: "))

if x < y:
    if x < z:
        minimum = x
    else:
        minimum = z
else: 
    if y < z:
        minimum = y
    else:
        minimum = z

print("The minimum value is: " + str(minimum))
********************************************************************
