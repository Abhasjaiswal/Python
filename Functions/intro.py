# A function is a block of code that performs a specific task.

#Types of function
#There are two types of function in Python programming:

#Standard library functions - These are built-in functions in Python that are available to use.
#User-defined functions - We can create our own functions based on our requirements.

#The syntax to declare a function is:

#def function_name(arguments):
    # function body 

#    return


def add(num1,num2):  #function with two arguements
     sum=num1+num2
     print(sum)


#call the function
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
sum=add(num1,num2)


def subtract(num1,num2):
     result=num1-num2
     return result

# call the function
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
result=subtract(num1,num2)
print(result)


#Python Library Functions
#In Python, standard library functions are the built-in functions that can be used directly in our program. For example,

#print() - prints the string inside the quotation marks
#sqrt() - returns the square root of a number
#pow() - returns the power of a number
#These library functions are defined inside the module. And, to use them we must include the module inside our program.

#For example, sqrt() is defined inside the math module.
import math

# sqrt computes the square root
square_root = math.sqrt(4)

print("Square Root of 4 is",square_root)

# pow() comptes the power
power = pow(2, 3)

print("2 to the power 3 is",power)
