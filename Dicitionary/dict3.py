"""Changing values using key names"""

# syntax: dict_name[Key] = value

car = {'brand':'Audi','Model':'Q7'}
 
car['Model']= 'S8'
print(car)

"""Changing values using update Method"""

# syntax: dict_name.update(dictionary)

car = {'brand':'Audi','Model':'Q7'}
car.update({'Model':"S7"})

print(car)


"""Adding new items using key name"""

# syntax: dict_name[new_key]="new_value"

car['Colour']="Black"
print(car)

"Adding new items using update() Method"

# syntax: dict_name.update(dictionary)
car = {'brand':'Audi','Model':'Q7'}

car.update({'Colour':'Blue'})
print(car)