"""String Slicing"""
"""A technique used to access a substring of a string"""

#For Example
string="Abhas Jaiswal"
print(string[0:10])

#This will produce output: Abhas Jais
"This happened because of string slicing. Lets provide idexing to the string. 0 is A and S is 9 but we need to provide 10 to print S."""

"""String Slicing With A Third Parameter"""

"1)Third Parameter is also called as step Value. By default,it is 1."
"2)Step value - 1 speicifies the number of elements to be skipped when slicing the string"
 
#for Example
string="Abhas Jaiswal"
print(string[0:10:2])

#This will produce AhsJi as the output 
"Lets check the step value. Since it is 2 we need to subtract 1 from the number specified. In our case it is 2-1=1 i.e we have to skip 1 word "
"Note: Whitespaces are also counted."

"3)Eliminating first and second parameter is allowed"
#To illustrate this let us take an example

string="abc"*3
print(string[::3]) #This will produce "aaa" as output 
"So, we dont need to specify the first and second parameter."
"Now lets understand why we got the output as aaa. so abc will pe printed thrice and step value will be 3-1=2 i.e we need to skip 2 words everytime.Therefore the output was aaa"

"Negative Third Parameter"

string="HELLO EVERYONE"
print(string[2:10:2])  #OUTPUT:LOEE
print(string[10:2:-2]) #OUTPUT: YEEO
"Here negative step value specified the direction. we need to add one to the step value"

#lets consider one more example

string="string"
print(string[5:0:-1]) # OUTPUT:gnirt 