# LOOP CONTROLS BREAK | CONTINUE
# BREAK STATEMENT

var=1
while(var<=15):
    if(var==10):
        break
    print (var)
    var=var+1
print ("We are out of the while loop")

while True:
    print ("Enter a digit")
    num=input()
    var=str(num)
    if(ord(var) in range(48,58)):
        break
print ("We are out of the while loop")

for val in "naresh":
    if val == "a":
        break
    print(val)

print("The end")
