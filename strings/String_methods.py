#Strip() Method
"Help in removing leading and trailing whitespaces in a string"

#For Example
print("    Hello World    ".strip()) #output: Hello World

"It can also remove any leading and trailing characters in a string"

#For example 
print("####Hello world######".strip("#")) #output: Hello world
 
#IMPORTANT
print(" ###Hello World####".strip("#"))
#OUTPUT:  ###Hello World 
#This happened because while checking it starts from the first word. In our case it is a whitespace therefore the strip method moves to the end part and removes it.

print("Hello World".strip("ldoH"))
#OUTPUT:ello Wor

#lstrip() Method
"By default, removes the leading whitespaces only"
#for example
print("  Hello World".lstrip())
#OUTPUT:Hello World
 
#We can also remove leading characters 
#for example
print("Hello world".lstrip("H"))
#OUTPUT : ello world


#rstrip Method
"By default, removes the trailing whitespaces only"
#for example
print("  Hello world      ".rstrip())
#OUTPUT:  Hello World


#split() Method
"It used to split the string into a list"
"Syntax: String.split(seperator,maxsplit)"

string="Hello!$I$am$Abhas".split('$',2)
print(string)
#OUTPUT: ['Hello!', 'I', 'am$Abhas']

string2="Hello! I am Abhas Jaiswal".split() #note:- If we dont specify any seperator & maxsplit then by default whitespace is treated a seperator and maxsplit as -1 (There's no limit )
print(string2)
#OUTPUT: ['Hello!', 'I', 'am', 'Abhas', 'Jaiswal']

#rsplit() Method
"Used to split the string from the right"
"Syntax: String.rsplit(seperator,maxsplit)"
string3="Hello!$I$am$Abhas".rsplit('$',2)
print(string3)
#OUTPUT: ['Hello!$I', 'am', 'Abhas']


#Join() Method
"Used to join the elements of an iterable"
"Syntax:seperator.join(iterable)"
"An iterable is an object which is cable of returning its members one at a time. List,Dictionary,tuple,set and strings are all iterables"

#For Example
L1=['H','e','l','l','o']
print("".join(L1))

#OUTPUT is Hello

L2=['I','am','Abhas','Jaiswal']
print(" ".join(L2))

#OUTPUT: I am Abhas Jaiswal

L3=['name','of','a','variable']
print("_".join(L3))
#OUTPUT : name_of_a_variable

D={'Name':'Abhas','Country':'India'}
print(" and ".join(D))
#OUTPUT: Name and Country

#replace() Method
"Used to replace a specified string with another string"
"Syntax: string.replace(oldstring,newstring,count)"

S= "I love Mangoes"
print(S.replace('Mangoes','strawberries'))
#output:I love strawberries
 
S="I love Strawberries"
print(S.replace(" ","-",2))
#output:I-love-Strawberries

#upper() Method
"Upper Method is used to convert all letter of the string to uppercase"
"syntax:sting.upper()" 
#Note: Upper() Method doesn't accept any arguements

#for example
string4="I am abhas Jaiswal"
print(string4.upper())


#lower() Method
"Lower Method is used to convert all the letters of the string to lowercase"
"syntax:string.lower()"


#for example
string5="I AM ABHAS JAISWAL"
print(string5.lower())



#capitalize Method
"Returns a character where the string is uppercase and rest are lowercase"

#for example
cap="maruti Suzuki"
print(cap.capitalize())


#isupper method
"Returns true if all characters are uppercase, otherwise returns false"

#for example
cap="maruti suzuki"
print(cap.isupper())

cap="MARUTI SUZUKI"
print(cap.isupper())


#islower method
"Return true if all the characters are lowercase, otherwise returns false"
cap="maruti suzuki"
print(cap.islower())

cap="MARUTI SUZUKI"
print(cap.islower())

#isaplha method
"Returns true if all the characters are alphabet(a-z or A-Z)"
cap="MarutiSuzuki"
print(cap.isalpha())

cap="123Maruti Suzuki"
print(cap.isalpha())


#isnumeric methid
"Returns true if all the characters are numbers (0-9)"
cap="12345678"
print(cap.isnumeric())

cap="A123456"
print(cap.isnumeric())
 
cap="1.23"  #will return false even if there is a dot
print(cap.isnumeric())


#isalnum Method
"Returns True if all the characters are alphanumeric (a-z or A-Z or 0-9)"

#for example
cap="ABC124"
print(cap.isalnum())

cap="ABHAS"
print(cap.isalnum())


#count() Method
"Finds the number of occurences of a substring in a given string"
"if the substring is not found, it returns 0 "
"Syntax: string.count(sub,start,end)"

#for example
cap="Hello I am Hello Hello"
print(cap.count("Hello"))

cap="I love fruits, fruits make me healthy"
print(cap.count("fruits",3,13))

#find Method
"Returns the occurence of the first occurence of the substring"
"if the substring is not found then it returns -1"
"syntax: string.find(sub,start,end)"

cap="I love fruits, fruits make me healthy"
print(cap.find("fruits")) #returns 7
print(cap.find("Abhas"))  #returns -1

cap="Python is a beautiful Language"
print(cap.find('b'))


#rfind Method
"Returns the index of the last occurence of the substring"

cap="Python is a beautiful Language"
print(cap.rfind("e"))


#index Method
"Return the index of the first occurence of the substring"
"If the substring is not found, it raises an exception(value error)"

cap="Python is a beautiful Language"
print(cap.index("c"))



#rindex Method
"Returns the index of the last occurence of the substring"
"If the substring is not found, it raises an exception(value error)"

cap="Python is a beautiful Language"
print(cap.rindex("c"))
