"""Introduction"""
# The if-else statement is used when the decesion has to be made among two alternatives.
# The if-elif statement is used when the decesion has to be made among more than two alternatives.

# syntax: if condition:
           #statment inside if
        #elif condition2:
           # statmenet inside elif
        #else:
           # statmement inside else 

# for example

x=5
if  x==5:
     print("x is 5")
elif x < 5:
     print("x is less than 5")
else:
     print("x is greater than 5")
print("DONE")

"""Program :Divisibility Test"""

# Write a program to check whether the number is divisible by 2 or 3

n=int(input("Enter the number: "))

if n%2==0:
     print("The number is visible by 2")
elif n%3==0:
     print("The number is divisible by 3")
else:
     print("The number is not divisble by 2 or 3")
