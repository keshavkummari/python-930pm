#!/usr/bin/python

def printinfo(name,*vartuple):

   print ("Output is: {}".format(name))

   for var in vartuple:
      print(var)
   return

#Call a function with single elements
#printinfo( 10 )

# Call a function with multiple elements
#printinfo( 70, 60, 50 )

#printinfo("Welcome to Python World","AWS","DevOps","CICD","Java","Django")

# Required Args
#printinfo("Guido","Rossum")

# KeyWord Args
#printinfo(firstname="Guido",lastname="Rossum")

# Default Args
#printinfo("Guido",lastname="Rossum")

# Variable-Length Args
printinfo("Guido Van Rossum","AWS","DevOps","CICD","Java","Django")
