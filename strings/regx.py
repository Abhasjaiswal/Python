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

txt='The rain in Spain'

#find all lower case characters alphabetically between "a" and "m"
x=re.findall("[a-m]",txt)
print(x)

txt1="hello planet"
# search for a sequence that starts with "he" followed by two(any) characters and an "o":
x = re.findall("he..o", txt1)
print(x)

#checks if the string ends with 'planet'
x=re.findall("planet$",txt1)
print(x)

#search for a sequence that starts with "he" followed by O or more(any) character, and an "o"

x=re.findall("he.*o",txt1)
print(x)

text="That will be 59 dollars"

# find all digit characters
x=re.findall("\d",text)
print(x)

#search for a sequence that starts with "he", followed exactly 2(any) characters, and an "o":
x=re.findall("he.{2}o",txt1)
print(x)

#search for a sequence that starts with "he", followed by 1 or more (any) characrers,and an "o"
x=re.findall("he.+o",txt1)
print(x)

new='The rain in Spain falls mainly in the plain!'
#check if the string contains either "falls" or "stays":
x=re.findall("falls|stays",new)
print(x)

if x:
     print("Yes, there is atleast one match")
else:
     print("No Match")

sentence='The rain in spain'

#check if the string starts with "The":
x=re.findall("\AThe",sentence)
print(x)

if x:
      print("Yes,there's a match")
else:
      print("No Match")

#check if "ain" is present at the beginning of a word:

x=re.findall(r"\bain",sentence)
print(x)

if x:
      print("Yes,there is at least one match")
else:
      print("No Match")

#check if "ain" is present at the end of a word:
x=re.findall(r"ain\b",sentence)
print(x)

if x:
      print("Yes,there's at least one match")
else:
      print("No Match")

#check if "ain" is present but NOT at the end of a word:

x=re.findall(r"ain\B",sentence)
print(x)

if x:
      print("Yes,there is at least one match")
      
else:
      print("No Match")
      
x=re.findall("\d",sentence)
print(x)
if x:
      print("Yes,there is at least one match")
      
else:
      print("No Match")

#return a match at every no-digit character:

x=re.findall("\D",sentence)
print(x)
if x:
      print("Yes,there is at least one match")
      
else:
      print("No Match")
     
sentence="The rain in Spain"
x=re.findall("\s",sentence)
print(x)
if x:
      print("Yes,there is at least one match")
      
else:
      print("No Match")