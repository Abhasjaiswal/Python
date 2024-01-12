#Let's dive into explanation of string comparison operators in Python:
"""
Points to Remember
1)Comparison Operators are case sensitive
2)Each Character has an ASCII value, and the ASCII Values of characters are compared
Example- ASCII Value of A=65 and ASCII Value of a=97
Therefore, A<a
"""

"""Certainly! Let's dive into a more descriptive explanation of string comparison operators in Python:
1.Equality (==):
The equality operator (==) checks whether two strings are identical.
It compares each character of the strings, and if all characters match, the result is True.
If there is any difference, the result is False
"""

#for example
str1="Hello"
str2="Hello"

print(str1==str2)

#This will return "True" as both the strings are identical

str1="Hello"
str2="hello"

print(str1==str2)

#This will return "False" as the strings are not identical 

"""
2.Inequality (!=):
The inequality operator (!=) checks if two strings are not identical.
If there is any difference between the strings, the result is True. 
If the strings are identical, the result is False.
"""

str1 = "hello"
str2 = "world"
print(str1!=str2)

#This will return 'True' as the strings are not identical 

str1="hello"
str2="hello"
print(str1!=str2)

#This will return 'False' as the string are identical 

"""
Greater Than (>) and Greater Than or Equal To (>=):
The greater-than operator (>) and greater-than-or-equal-to operator (>=) compare strings lexicographically.
It checks if one string comes after the other in dictionary order.
This is determined by comparing the Unicode values of the characters
"""

str1="Hello"
str2="hello"
print(str1>str2)
 
# The ASCII value of h is 104 and H is 72
# since 72 is not greater than 104 therefore the output will be false 

#Let's generate a case where we can implement >=

str1="Hello"
str2="Hello"

print(str1>=str2)

#it will return true because str1 = str2 
#similarly,
"""
Less Than (<) and Less Than or Equal To (<=):
The less-than operator (<) and less-than-or-equal-to operator (<=) also compare strings lexicographically.
It checks if one string comes before the other in dictionary order.
"""
