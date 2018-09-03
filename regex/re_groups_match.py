import re
'''
text = 'This is some text -- with punctuation.'

print (text)
print()

for pattern in [ r'^(\w+)',           # word at start of string
                 r'(\w+)\S*$',        # word at end of string, with optional punctuation
                 r'(\bt\w+)\W+(\w+)', # word starting with 't' then another word
                 r'(\w+t)\b',         # word ending with 't'
                 ]:
    regex = re.compile(pattern)
    match = regex.search(text)
    print('Matching "%s"' % pattern)
    print('  ', match.groups())
    print()
'''

"""
If you are using grouping to find parts of the string,
but you don’t need all of the parts matched by groups,
you can ask for the match of only a single group with group().
"""
import re

text = 'This is some text -- with punctuation.'

print ('Input text            :', text)

# word starting with 't' then another word
regex = re.compile(r'(\bt\w+)\W+(\w+)')
print ('Pattern               :', regex.pattern)

match = regex.search(text)
print ('Entire match          :', match.group(0))
print ('Word starting with "t":', match.group(1))
print ('Word after "t" word   :', match.group(2))

"""
Group 0 represents the string matched by the entire expression,
and sub-groups are numbered starting with 1 in the order their left
parenthesis appears in the expression.
"""
