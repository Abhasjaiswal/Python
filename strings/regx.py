#Regular expressions, often abbreviated as "regex" or "regexp," are a powerful tool for pattern matching and searching within text data. Python's re module provides support for working with regular expressions.

#Import the re Module
#Before using regular expressions in Python, you need to import the re module.

import re 
s='geeks.forgeeks'

#Without Using
match=re.search(r'.',s)
print(match)

#Using \
match = re.search(r'\.',s)
print(match)

