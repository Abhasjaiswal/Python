# INPUT() METHOD
"""Used to take input from the user"""
"""User input is always converted to a string"""

#for example
name=input()
print(name)
print(type(name))


#INPUT METHOD WITH A MESSAGE

"""Syntax: Input('Message')"""
number=input('Enter a number: ')
print(number)
print(type(number))


#Typecasting the user input
"""Typecasting is needed to convert the string to integer"""
"""Input() Method can be provided as an arguement to the int() method"""
 
#FOR EXAMPLE
number=int(input("Enter the number: "))
print(number)
print(type(number))
"""Input() Method"""
# Used to take input from the user 
# User input is always converted to a string 

# For example 
name=input()
print(name)
print(type(name))   # str

"""Input Method with a message"""
# syntax: Input("Message")

name2=input("Enter your name:")
print(name2)

number=input("Enter the number:")
print(number)
print(type(number))   # Here the number is treated as string not an integer

# In order to take a number from the user as an integer using int() method

number=int(input("Enther the number"))
print(number)
print(type(number))  # the type is int


