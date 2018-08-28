# Program to add natural
# numbers upto n where
# n is provided by the user
# sum = 1+2+3+...+n

# take input from the user
n = int(input("Enter n: "))

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1      # update counter

# print the sum
print("The sum is",sum)
