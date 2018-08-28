#!/usr/bin/python

while True:
    print ("Enter a digit")
    num=input()
    #var=str(num)
    if(ord(num) in range(48,58)): # Decimal 0-9
        break
        #continue
print ("We are out of the while loop")
