"""Removing Dictionary Items"""

# 1. Removing an item using pop() Method - removes an item using the key of the item. It also return the deleted item's value 
"""Syntax: dict_name.pop(key)"""

car = {'brand':'Audi','Model':'Q7'}

car.pop('Model')
print(car)

# 2. Removing an item using popitem() Method - removes the last inserted item and it returns the deleted item as a tuple 
"""Syntax: dict_name.popitem()"""

car = {'brand':'Audi','Model':'Q7'}
car.popitem()
print(car)

# 3. Removing an item using del keyword
"""syntax: del dict_name[key]"""

car = {'brand':'Audi','Model':'Q7'}
del car['Model']
 
# 4. Removing a dictionary using del keyword - removes an entire dictionary

car = {'brand':'Audi','Model':'Q7'}
del car

# 5. Empty a dictionary using clear method()
"""Syntax: dict_name.clear()"""

car = {'brand':'Audi','Model':'Q7'}
car.clear()
print(car)

