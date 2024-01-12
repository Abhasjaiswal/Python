"""
string Formatting Operator
1. String Formatting Operator(%)is used to format a string
2. %d , %c , %s and %f are some commonly used string formatters
"""
#For Example
age=28
print("My Age is %d"%(age)) #OUTPUT:My Age is 28

#Since 28 is an integer, therefore I have specified %d and the number 28 will be placed at %d.

"Interpolation:Interpolation is the insertion of something of a different nature into something else."
"String Interpolation/Formatting:The process of inserting a pre defined string interpolation or string formatting"

# %Formatting
"This is the oldest technique used to insert an objec into a strng"
name="Abhas"
print("My name is %s" %(name))  #OUTPUT: My name is Abhas

"Mutiple Variables Are Allowed"
name="Abhas"
city="Bengaluru"
print("My name is %s and I live in %s" %(name,city)) #OUTPUT: My name is Abhas and I live in Bengaluru

"str format()Function"

#In this technique, the place holders are replaced by curly braces
name="Abhas"
city="Bengaluru"
print("My name is {} and I live in {}" .format(name,city)) #OUTPUT:My name is Abhas and I live in Bengaluru

"Refrencing Variable through indexing is allowed"
name="Abhas"
city="Bengaluru"
print("My name is {0} and I live in {1}" .format(name,city)) #OUTPUT:My name is Abhas and I live in Bengaluru

#Here 0 refers to the variable "name" and 1 refers to the variable city

name="Abhas"
city="Bengaluru"
print("My name is {1} and I live in {0}" .format(name,city)) #OUTPUT:My name is Bengaluru and I live in Abhas


#Format Specifiers like f for float , b for binary , d for integer is used 

print("I got {0:f}% marks in English ".format(55.66))

#{0:f} 0 specifies the index and The first value in the format method will be treated as a float

"""An Integer can be provided in the place of float"""
print("I got {0:f}% marks in English ".format(55))
#here I have changed the value 55.66 to 55 which is an integer


#The length of the value after the deciman point can be controlled
print("I got {0:.2f}% marks in English ".format(55.785673495))
#OUTPUT: I got 55.79% marks in English 

