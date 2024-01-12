"1.Implicit Type Conversion"
#Ability of Python to convert an object from one data type to another without any intervention from the programmer.

#Rule of Conversion - Lower Data type is coverted to the higher data type.

#for example
x=15.90
y=5   #Python will implicitly convert 5 to 5.0 (int to float)
print(x+y)

#Dividing two integer always results in floating point value

#for example
print(5/5)  #output:1.0

#Note:- The type of resultant depends upon the operator and value with higher data type

#In python, implicit conversion of higher data type to lower data type is not possible.


"2.Explicit Type Conversion"
"A.using int()"

#Refers to the conversion of object of one type to integer via programmer's intervention

"Syntax: int(value,base)"

#For Example
x="100" 
print(type(x)) #OUTPUT: <class 'str'>

print(int(x))  #converted 'str' to 'int'

print(int(x,2)) # Base:2 specifies that the number 'x' will be treated as binary. 

"B.Using float()"

#Refers to the conversion of object of one type to float type via programmer's intervention

"Syntax:float(value)"

x=78     #integer 
x=float(78)  #converted int to float type
print(x)


"C.Using Str"

#Refers to the conversion of object of one type to string type via programmer's intervention
 
"Syntax:str(value)"

num=123
result=str(num)
print(result)
print(type(result))







