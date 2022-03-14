"""
Regular Expression

A regular expression is a special sequence of characters that helps you match or find 
other strings or sets of strings, using a specialized syntax held in a pattern.

To implement regular expression in Python there is a inbuild module re.

The two majorly used functions form this modules are
search
match

Syntax:

re.search(pattern, string, [flags = 0])

re.match(pattern, string, flags = 0)

"""

import re

# print(dir(re))

####Match#####

ph = input("Please enter your phone number")

p = re.match(r'([7,8,9])([0-9]{9})', ph)
# r'' inside the quotes we can write our pattern for matching
# () are groups
# [] are list of char
# {} are no. of exact occurances

if p:
    print("valid")
else:
    print("Invalid")


add = input("Enter your Address")

a = re.match(r'.*', add)  # * is 0 or more(till inifnity) occurances

if a:
    print("valid")
else:
    print("Invalid")
