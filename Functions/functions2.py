#Python Function Arguments
#Arguments are the values passed inside the parenthesis of the function. A function can have any number of arguments separated by a comma.

#example
# A simple Python function to check
# whether x is even or odd
def evenOdd(x):
	if (x % 2 == 0):
		print("even")
	else:
		print("odd")


# Driver code to call the function
evenOdd(int(input("enter the number: ")))

#Types of Python Function Arguments
#Python supports various types of arguments that can be passed at the time of the function call. In Python, we have the following 4 types of function arguments.

#Default argument
#Keyword arguments (named arguments)
#Positional arguments
#Arbitrary arguments (variable-length arguments *args and **kwargs)


#1. Default Argument - Default arguments are parameters in a function that have a default value. If a value is not provided for these parameters during the function call, the default value is used.
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("John")  # Uses default greeting value
greet("Alice", "Hi")  # Provides a custom greeting

# 2. Keyword Arguments (Named Arguments): Keyword arguments are passed to a function using the parameter names. This allows you to specify which argument corresponds to which parameter, regardless of the order.

def calculate_power(base, exponent):
    result = base ** exponent
    return result

print(calculate_power(base=2, exponent=3))

# 3.Positional Arguments:Positional arguments are the most common type of arguments. They are passed to a function based on their position in the function call. The order matters.

def add_numbers(a, b):
    result = a + b
    return result

print(add_numbers(3, 5))

# 4. Arbitrary Positional Arguments (*args): If you want a function to accept a variable number of positional arguments, you can use *args.The *args collects any additional positional arguments into a tuple.

def add_numbers(*args):
    result = 0
    for num in args:
        result += num
    print(result)

add_numbers(2, 3, 5,6,7,8,9) 


#Arbitrary Keyword Arguments (**kwargs):
#If you want a function to accept a variable number of keyword arguments, you can use **kwargs.
#The **kwargs collects any additional keyword arguments into a dictionary.
#Example:

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="John", age=25, city="New York")

#5. Combining Both (*args and **kwargs):
#You can use both *args and **kwargs in the same function definition to allow for maximum flexibility.
#Example:
def display_info(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info("John", 25, city="New York", occupation="Engineer")
