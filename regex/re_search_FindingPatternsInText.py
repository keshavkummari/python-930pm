# Finding Patterns in Text: 
import re

patterns = [ 'this', 'that' ]
text = 'Does this text match the pattern?'

for pattern in patterns:
    print ('Looking for "%s" in "%s" ->' % (pattern, text),)

    if re.search(pattern,  text):
        print ('found a match!')
    else:
        print ('no match'    )
"""        
The Match object returned by search() holds information about the nature of 
the match, including the original input string, the regular expression used, 
and the location within the original string where the pattern occurs.
"""
import re
pattern = 'this'
text = 'Does this text match the pattern?'

match = re.search(pattern, text)

s = match.start()
e = match.end()

print ('Found "%s" in "%s" from %d to %d ("%s")' % \
    (match.re.pattern, match.string, s, e, text[s:e]))
"""
The start() and end() methods give the integer indexes into the string showing
where the text matched by the pattern occurs.        
"""
