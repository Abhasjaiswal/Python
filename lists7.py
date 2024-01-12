"Introduction to List Comprehension"
# provides a shorter syntax while creating a new list from an existing list

names=['John','James','Emmy','Micheal','Jimmy']

j_names=[]

for name in names:
     if 'J' in name:
          j_names.append(name)
          
print(j_names)


# SHORTER METHOD

j_names=[name for name in names if 'J' in name]
print(j_names)


"The Syntax"

"""List=[expression for item in iterable if condition==True]"""

# The condition is optional

#lets cosider an example where we wont provide the condition

names=['John','James','Emmy','Micheal','Jimmy']

names_copy= [name for name in names]
print(names_copy)
