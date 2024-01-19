#Iterating over a dictionary -  for loops can be used to iterate over a dictionary

course={'name':'Abhas','Age':'20'}
for x in course:
     print(x)
     
# Accessing values of a dictionary - Values can be accessed using square-bracket notation
course={'name':'Abhas','Age':'20'}
for x in course:
     print(course[x])

# Values can also be accessed usig values() Method
course={'name':'Abhas','Age':'20'}
for x in course.values():
     print(x)


#Accessing keys of a dictionary - keys can be accessed using keys() method
course={'name':'Abhas','Age':'20'}
for x in course.keys():
     print(x)


# Keys and values can be accessed using items() method
course={'name':'Abhas','Age':'20'}
for x,y in course.items():
     print(x,y)
    

