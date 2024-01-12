#F-Strings
"It is used to format a string"
#Syntax:f"String {object}"
#note: We are free to use F or f and '' or " "

#For Example
name="ABHAS"
city="BENGALURU"
print(f"My name is {name} and I live in {city}")
print(F'My name is {name} and I live in {city}')

"Call to method of the string is possible"
name="Abhas"
city="bengaluru"
print(f"My name is {name.upper()} and I live in {city.upper()}")
print(f"My name is {name.lower()} and I live in {city.lower()}")
#By specifying upper and lower we can print the word in lower case and upper case as required

#MULTILINE F-STRING

name="ABHAS"
city="BENGALURU"
age=20

introduction=f"My name is {name}.\
My age is {age}\
 and I live in {city}"
print(introduction)
