# Bitwise AND OPERATION:
True  = 1
False = 0

a=15
b=10

print(bin(a))
'0b1111'

print(bin(b))
'0b1010'

print("Results of" ,bin(a), "AND" ,bin(b),bin(a&b))
'0b1010'

0b1111
0b1010
-------
  1010  # Output (Results will be true when both bits are true)
-------
# Bitwise OR OPERATION:
print(bin(a))
'0b1111'

print(bin(b))
'0b1010'

print(bin(a|b))
'0b1111'

0b1111
0b1010
-------
  1111
-------

# Output (Results will be true even if any one of the two
bits it's true)

# Bitwise XOR OPERATION:
print(bin(a))
'0b1111'

print(bin(b))
'0b1010'


print(bin(a^b))
'0b101'

0b1111
0b1010
-------
  0101  # Output 1+1=0 1+0=1 1+1=0 1+0=1
  (Bits has to be differenet then its true condition)
-------
