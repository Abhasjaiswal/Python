"""Input a list using split() Method in Python"""

# We know that the split Method is used to slpit a string into substrings.
# Syntax: String.split(seperator,maxsplit)


# For example
name= "I am John"
print(name.split())


"""Accepting a list of numbers with split() Method is easier"""

#Example: Create a list of numbers 67,80,95 and 5.
numbers=input("Enter the numbers: ").split()
print(numbers)


"""Basics of For loop"""
 
# For Loop is used to repeat a specific code a certain number of times.

for i in range(0,3):
     print("Hello World!")
     
"""Accepting a list using split() and for Loop"""

n=int(input("Enter the number of elements: "))
numbers = input("Enter the Numbers: ").split()

for i in range(0,n):
     numbers[i]=int(numbers[i])
     

print(numbers)
print(type(numbers[0]))

