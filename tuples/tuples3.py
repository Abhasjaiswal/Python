"""Adding items to a tuple"""
# It is not possible to add items to the tuples directly as tuples are immutable
# Workaround: We can convert tuple to a list and then add the item and then convert back list to tuple

cars=('BMW','Mercedes','Mercedes','Ford')
temp=list(cars)
temp.append('Toyota')
print(temp)
cars = tuple(temp)
print(cars)

"""Updating items of a tuple"""

# It is not possible to update items as tuples are immuatable therefore we have to follow a workaround 

cars=('BMW','Mercedes','Mercedes','Ford')
temp =list(cars)
temp[0]='Ferrari'
print(temp)
cars =tuple(temp)
print(cars)


"""Removing items from a tuple"""

# Again it is not possible to remove an item from a tuple as it is immutable therefore we have to follow a workaround

cars=('BMW','Mercedes','Mercedes','Ford')
temp=list(cars)
temp.remove('Ford')
print(temp)
cars=tuple(temp)
print(cars)

"""Removing entire tuple using del keyword"""

cars=('BMW','Mercedes','Mercedes','Ford')
del cars
#print(cars)
