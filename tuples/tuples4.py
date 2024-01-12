"""Unpacking a tuple"""
# Packing means assigning values to a tuple
# Unpacking means extracting values of a tuple

cars=('BMW','Mercedes','Mercedes')
car1 , car2 , car3= cars
print(car1)
print(car2)
print(car3)


"""Use of Asterisk"""
# used when the number of variables are less than the values of a tuple

cars=('BMW','Mercedes','Mercedes','Ford')

car1,car2,*car3=cars
print(car1)
print(car2)
print(car3)


# If asterisk is used with a variable other than the last variable, then the values are assigned untill the values left mateches the variables left
cars=('BMW','Mercedes','Mercedes','Ford')


car1,*car2,car3=cars
print(car1)
print(car2)
print(car3)
