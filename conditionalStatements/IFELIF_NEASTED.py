#!/usr/bin/python

char=input("Please enter any charcter : ")

if ord(char)>=65 and ord(char)<=90:
    print ("You entered an upper case alphabet")
    if char in ['A','E','I','O','U']:
        print ("You entered A vowel.",char)
    else:
        print ("You entered a consonant.", char)
elif ord(char)>=97 and ord(char)<=122:
    print ("You entered a lower case alphabet.", char)
    if char in ['a','e','i','o','u']:
        print ("You entered a vowel.", char)
    else:
        print ("You entered a consonant.", char)
else:
    print ("You did not enter an alphabet.", char)

print ("We are out of the if..elif block")
