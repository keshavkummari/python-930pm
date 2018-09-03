"""
Python extends the basic grouping syntax to add named groups.
Using names to refer to groups makes it easier to
modify the pattern over time,
without having to also modify the code using the match results.

To set the name of a group, use the syntax (P?<name>pattern).
"""
import re

text = 'This is some text -- with punctuation.'

print(text)
print()

for pattern in [ r'^(?P<first_word>\w+)',
                 r'(?P<last_word>\w+)\S*$',
                 r'(?P<t_word>\bt\w+)\W+(?P<other_word>\w+)',
                 r'(?P<ends_with_t>\w+t)\b',
                 ]:
    regex = re.compile(pattern)
    match = regex.search(text)
    print('Matching "%s"' % pattern)
    print('  ', match.groups())
    print('  ', match.groupdict())
    print()
'''
Use groupdict() to retrieve the dictionary mapping group names
to substrings from the match.

Named patterns are included in the ordered sequence returned by groups(),
as well.
'''
