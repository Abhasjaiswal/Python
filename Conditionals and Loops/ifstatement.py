"""Introduction"""
# Decides whether a particular statemement or block of statements will be executed or not. 
# Syntax: if condition:  (An expression that evaluates to a boolean value true or false)
#            statement1 
#            statement2 

# For example
x=10
if x < 50: 
     print("X is less than 50")


# The statement outside the if block will be executed regardless of whether the condition in the if statement is sastisfied or not 
# Syntax: if condition:
#           Statement inside if block
#         statement outside if block 

# For example
x= 60 
if x<50:
     print("x is less ")
print("End of the program")


"""The Short Hand if"""
# when only one statement to execute, put that in same line as the if statement 
# syntax: if condition: #statement 

x=10
if x<50: print("x is less than 50")
print("End of the program")

"""Nested If Statement"""
# The if statement inside another if statement is called nested if statement. 

# syntax: if condition1:
#         executes when the condition1 is true
#          if condition2:
#          executes when the condition2 is true
# statement outside if block 
 
# For example
x=10
if x<50:
     if x==10:
          print("x is equal to 10")
     print("x is less than 50") 
print("End of the program")

