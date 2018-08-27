#!/usr/bin/python

char=input("Enter a lower or upper case letter i.e. only consonants: ")

if ord(char)>=65 and ord(char)<=90:
    print ("You entered an upper case alphabet")
    if char in ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']:
        print ("You entered a consonant.")
    else:
        print ("ABC")
elif ord(char)>=97 and ord(char)<=122:
    print ("You entered a consonant")
    if char in ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']:
        print (char,"You entered a consonant.")
    else:
        print ("abc")
else:
    print ("You did not enter an alphabet.")
print ("We are out of the if..elif block")
