import re

# Lets use a regular expression to match a few date strings.
regex = r"[a-zA-Z]+ \d+"
matches = re.findall(regex, "June 24 August9 Dec 12",re.M|re.I)

for match in matches:
    # This will print:
    #   June 24
    #   August 9
    #   Dec 12
    print ("Full match: %s" % (match))

# To capture the specific months of each date we can use the following pattern
regex = r"([a-zA-Z]+) \d+"
matches = re.findall(regex, "June 24, August 9, Dec 12")
for match in matches:
    # This will now print:
    #   June
    #   August
    #   Dec
    print ("Match month: %s" % (match))

# If we need the exact positions of each match
regex = r"([a-zA-Z]+) \d+"
matches = re.finditer(regex, "June 24, August 9, Dec 12")
for match in matches:
    # This will now print:
    #   0 7
    #   9 17
    #   19 25
    # which corresponds with the start and end of each match in the input string
    print ("Match at index: %s, %s" % (match.start(), match.end()))




