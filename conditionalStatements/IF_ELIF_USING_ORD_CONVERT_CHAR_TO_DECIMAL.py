#!/usr/bin/python

char=input("Please enter a vowel from A|a|E|e|I|i|O|o|U|u : ")

if ord(char)>=65 and ord(char)<=90:
    print ("You entered an upper case alphabet")
    if char in ['A','E','I','O','U']:
        print ("You entered Upper Case vowel i.e.",char)
    else:
        print("You entered Upper Case consonant i.e.", char)
elif ord(char)>=97 and ord(char)<=122:
    print ("You entered a Lower case alphabet")
    if char in ['a','e','i','o','u']:
        print ("You entered Lower Case vowel.", char)
    else:
        print("You entered Lower Case consonant i.e.", char)
else:
    print ("You did not enter an alphabet.")
    
print ("We are out of the if..elif block")
