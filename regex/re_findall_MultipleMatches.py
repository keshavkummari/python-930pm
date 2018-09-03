# Multiple Matches :

"""
So far the example patterns have all used search()
to look for single instances of literal text strings.

The findall() function returns all of the substrings of the
input that match the pattern without overlapping.
"""

import re

text = 'abbaaabbbbaaaaaab'

pattern = 'ab'

for match in re.findall(pattern, text):
    print('Found "%s"' % match)
