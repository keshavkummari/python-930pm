#!/usr/bin/python

char=input("Enter a Upper Case or Lower Case Vowel: " )

if ord(char)>=65 and ord(char)<=90:
    print ("You entered an upper case alphabet")
    if char in ['A','E','I','O','U']:
        print ("You entered", char ,"vowel.")
    else:
        print ("You entered a consonant.")
elif ord(char)>=97 and ord(char)<=122:
    print ("You entered a vowel.")
    if char in ['a','e','i','o','u']:
        print ("You entered a vowel.")
    else:
        print ("You entered a consonant.")
else:
    print ("You did not enter an alphabet.")
print ("We are out of the if..elif block")
