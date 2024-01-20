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
