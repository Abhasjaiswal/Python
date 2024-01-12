"""Use of Logical AND with If statement"""
# used to combine multiple conditions into a single expression
# Helpls in avoiding the use of nested if statements

# FOR EXAMPLE
age=20
nationality='Indian'

if age>18:
     if age <30:
          if nationality=='Indian':
           print("You are elgiible for the exam ")


# WE CAN USE LOGICAL AND 
age=20
nationality='Indian'

if age>18 and age <30 and nationality=='Indian':
     print("You are eligible for the exam")


"""Logical AND with if-else statememt"""
# If any one condition is not satisfied, then the else block will be executed


age=32

if age>18 and age <30 and nationality=='Indian':
     print("You are eligible for the exam")
else:
     print("You are not eligible for the exam")

"""Logical AND with if-elif-else statement"""


age=20
nationality='American'

if age>18 and age <30 and nationality=='Indian':
     print("You are eligible for the exam. Exam fee is 1500 Ruppees")
elif age>18 and age <30 and nationality=='American':
     print("You are eligible to vote. Exam fees is 50 Dollars")
else:
     print("You are not eligible for the exam")


"""Use of LOGICAL OR with if statement"""

today='sunday'

if today=='saturday' or today=='sunday':
     print("It is weekend ")


"""Use of LOGICAL OR with if-else statement"""

today='Monday'

if today=='saturday' or today=='sunday':
     print("It is weekend ")
else:
     print("It is a weekday")

# similarly we can use logical OR with if-elif-else statement 


"""Logical NOT with a boolean Value"""
# If the Boolean value is true then then NOT operator returns false.

x=False

if not x:
     print("x is false")


"""Logical NOT with a string"""
# if the string is empty then the NOT  operator will return true

name='John'

if not name:
     print("NO NAME")
else:
     print(f"your name is {name}")


name=''

if not name:
     print("NO NAME")
else:
     print(f"your name is {name}")


"""Logical NOT with a list, dictionary and tuple"""
# if a list , dictionary or tuple is empty then the NOT operator will return true.

names=['John','Mike','Abhas']
if not names:
     print("The list is empty")
else:
     print(f"there are a total of {len(names)} names in the list.")

names=[]
if not names:
     print("The list is empty")
else:
     print(f"there are a total of {len(names)} names in the list.")
