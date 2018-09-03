# Compiling Expressions :   
"""
re includes module-level functions for working with regular expressions as 
text strings, but it is usually more efficient to compile the expressions 
your program uses frequently. 

The compile() function converts an expression string into a RegexObject.
"""    
import re

# Pre-compile the patterns
regexes = [ re.compile(p) for p in [ 'this',
                                     'that',
                                     ]
            ]
text = 'Does this text match the pattern?'

for regex in regexes:
    print ('Looking for "%s" in "%s" ->' % (regex.pattern, text),)

    if regex.search(text):
        print ('found a match!')
    else:
        print ('no match')

print("*******************************")
"""
The module-level functions maintain a cache of compiled expressions,
but the size of the cache is limited and using compiled expressions
directly means you can avoid the cache lookup overhead.

By pre-compiling any expressions your module uses when the module is loaded you
shift the compilation work to application startup time,
instead of a point where the program is responding to a user action.
"""

"""
finditer() returns an iterator that produces Match instances instead
of the strings returned by findall().
"""
import re

text = 'abbaaabbbbaaaaa'

pattern = 'ab'

for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))

"""
This example finds the same two occurrences of ab,
and the Match instance shows where
they are in the original input.
"""
