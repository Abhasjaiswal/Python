#A Generator in Python is a function that returns an iterator using the Yield keyword

#Create a Generator in Python
#In Python, we can create a generator function by simply using the def keyword and the yield keyword. The generator has the following syntax in Python:

#def function_name():
#    yield statement 

# A generator function that yields 1 for first time, 
# 2 second time and 3 third time 
def simpleGeneratorFun(): 
	yield 1			
	yield 2			
	yield 3			

# Driver code to check above generator function 
for value in simpleGeneratorFun(): 
	print(value)

#Generator Object
#Python Generator functions return a generator object that is iterable, i.e., can be used as an Iterator. Generator objects are used either by calling the next method of the generator object or using the generator object in a “for in” loop.
#Example:In this example, we will create a simple generator function in Python to generate objects using the next() function.

# A Python program to demonstrate use of 
# generator object with next() 

# A generator function 
def simpleGeneratorFun(): 
	yield 1
	yield 2
	yield 3

# x is a generator object 
x = simpleGeneratorFun() 

# Iterating over the generator object using next 

# In Python 3, __next__() 
print(next(x)) 
print(next(x)) 
print(next(x))

