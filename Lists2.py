# Adding Elements to a List
"""Elements can be added to a list in different ways,following are the methods to add elements to the list"""

"""1.append() Method"""
"""2.Insert() Method"""
"""3.Extend() Method"""

# 1.append() Method
"""A built in method used to add an item at the end of a list"""
# Syntax list.append(value)

#for example
languages=['Python','Java','c']
languages.append('C++')
print(languages)

# we can add as many elements as we want 
languages.append('Ruby')
print(languages)

#we can also add a list in the existing list
languages.append(['html','css'])
print(languages)


#2. Insert() Method
"""A built in method to add an item at a specific position."""
"""Syntax: list.insert(position,value)"""

Programming=['Python','C']
Programming.insert(0,'java')
print(Programming)


# 3.Extend() Method
"""A built in Method used to add all items of one list in another list"""
"""syntax: list1.extend(list2)"""

#for example
Programming.extend(languages)
print(Programming)



