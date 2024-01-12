"""Introduction"""
# The else statement can be used with if statement to execute a block of code when the condition is not satisfied.
# syntax: if condition:
           #statement inside if
#        else:
          #statement inside else
    #statement outside if and else block 

# For example
age=20
if age < 18:
     print("you can't vote")
else:
     print("you can vote")
print("End of the program")


"""The short Hand if-else"""
# Used when only one statement for if and one statement for else needs to be executed
# syntax: if statement if condition else else condition
 
# for example
age=20
print("you can't vote") if age <18 else print("you can vote")

