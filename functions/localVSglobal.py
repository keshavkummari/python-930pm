#!/usr/bin/python

_global0,_global1 = 100,200

def multiply(numberOne, numberTwo):
    'This function multiplies'
    abc = numberOne*numberTwo
    print (abc)
    print (_global0)
    print (_global1)
    return

multiply(_global0,_global1)
#multiply(10,20)


#!/usr/bin/python

total = 0 # This is global variable.

# Function definition is here
def intel( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2 # Here total is local variable.
   print ("Inside the function local variable called total : ", total)
   return total

# Now you can call sum function
print ("Before calling intel function : ", total)

intel( 10, 20 )

print ("Outside the function global variable total : ", total)

abc = intel(5,10)
print(abc)

#!/usr/bin/python

total = 0; # This is global variable.

# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   print ("Inside the function local total : ", total)
   return

# Now you can call sum function
sum( 10, 20 );
print ("Outside the function global total : ", Total )

