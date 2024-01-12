"""Introduction to Tuples"""
# A collection of items which are indexed,ordered and are immutable
# Syntax: tuple_name = (item1,item2,item3...)

# FOR EXAMPLE
cars=('Mercedes,BMW,Audi')
print(cars)

# Tuples are immuatable i.e. we cannot change any item
#cars[0]='Ford'  will throw an error

# Tuples can have duplicates
cars=('BMW','Mercedes','Mercedes','Ford')
print(cars)


#Tuple with one item
# syntax: tuple_name = (item1,) (We have to mention comma after the item else it will be considered as a string)
cars=("BMW",)
print(cars)


# Length of a Tuple 
"""Can be determined using the len() function"""

cars=('BMW','Mercedes','Mercedes','Ford')
print(len(cars))


# TUPLE() CONSTRUCTOR is an alternative way to create a tuple
cars=tuple(('BMW','Mercedes','Mercedes','Ford'))
print(cars)

