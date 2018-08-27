#!/usr/bin/python

star = int(input("Please give us rating between 1 and 5\n"))

if star <= 0 or star >= 6:
    print("Please enter a valid number\n")
    exit()

if star == 1:
    print("Your rating was 1")
elif star == 2:
    print("Your rating was 2")
elif star == 3:
    print("Your rating was 3")
elif star == 4:
    print("Your rating was 4")
else:
    print("Your rating was", star)
