"""Accessing Tuple Items through positive indexing"""

# Each item of a tuple can be accessed through its index
# Syntax: tuple_name[index]

cars=('BMW','Mercedes','Mercedes','Ford')
print(cars[1])


# Trying to access item out of the index range will result an index error.
# Providing float or any other data type to the index will result in typeerror.


"""Accessing Tuple Items through negative indexing """

#Index -1 refers to the last item of the tuple , -2 refers to the second last item and so on.
cars=('BMW','Mercedes','Mercedes','Ford')
print(cars[-1])


"""Accesing tuple items through slicing"""
# Range of items can be accessed using slicing 
# Syntax: tuple_name[index1:index2]

cars=('BMW','Mercedes','Mercedes','Ford')
print(cars[1:3])
print(cars[1:])
