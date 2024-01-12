"""Accessing values using key names"""

# syntax: dict_name[key]

car = {'brand':'Audi','Model':'Q7'}

print(car['brand'])


"""Accessing values using get() Method"""

#syntax: dict_name.get(key)

car = {'brand':'Audi','Model':'Q7'}
print(car.get("brand"))


"""Accessing keys using keys() Method"""

# returns a view object containing key as a list.
# view object reflects any changes done to the dictionary

# Syntax: dict_name.keys()
car = {'brand':'Audi','Model':'Q7'}
car_keys=car.keys()
print(car_keys)

car['fueltype']='diesel'
print(car_keys)


"""Accessing values using values() Method"""
# returns a view object containing values as a list.
# syntax: dict_name.values()

car = {'brand':'Audi','Model':'Q7'}
car_vales=car.values()
print(car_vales)

car['fuel type']='diesel'
print(car_vales)


"""Accessing items using items() Method"""

# returns a view objects containing item as a list
# syntax: dict_name.items()

car = {'brand':'Audi','Model':'Q7'}
car_items=car.items()
print(car_items)

car['fuel type']='diesel'
print(car_items)
