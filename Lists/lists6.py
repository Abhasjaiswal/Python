"""Removing List items in Python"""

# 1. Remove() Method - Removes the specified item.

List=["Abhas","Jaiswal","name"]
List.remove("Abhas")
print(List)


# Pop() Method - used to remove an item at the specified index

List=["Abhas","Jaiswal","name"]
List.pop(1)  #if the index is not mentioned then the last element from the list will be removed
print(List)

# Del Keyword method - removes an item at the spcified index

List=["Abhas","Jaiswal","name"]
del List[2]

# Using del we can also remove the list completely

del List


# Clear the list using clear() Method

List=["Abhas","Jaiswal","name"]
List.clear()
print(List)
print(List)

