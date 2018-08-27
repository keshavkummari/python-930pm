TempeRature = float(input("Enter a temperature ")) * 9.0 / 5 + 32

print("That degrees converts to",TempeRature)

if TempeRature > 212:
    print("Steam")
elif TempeRature > 112:
    print("Very Hot Water")
elif TempeRature > 32:
    print("Water")
else:
    print("Ice")
print("Program completed")
