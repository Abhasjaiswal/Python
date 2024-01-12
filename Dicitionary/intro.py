"""Introduction to Dictionaries"""
# A collection of key-value pairs
# Syntax: dict_name={key1: Value1, key2: value2 ...}
 
# FOR EXAMPLE

car = {'brand':'Audi','Model':'Q7'}
print(car)

# it cannot have two items with same key

car = {'brand':'Audi','Model':'Q7','Model':'Q8'} #is not allowed
print(car)  # in such type of case the last value will be stored "Q8"

# Dictionaries are mutable 

car = {'brand':'Audi','Model':'Q7'}
car['Model']='Q9'

print(car)

"""Length of a Dictionary"""

# can be determined using len() function
# it gives the count of key-value pairs of a dicitionary 

car = {'brand':'Audi','Model':'Q7'}
print(len(car))


"The dict() constructor- An alternative way to create a dictionary"""

car=dict(brand ="Audi",model="q7")
print(car)