#Introduction to Lists in Python

"""A list is a collection of similar or different types of data items."""

#Example: A list of 10 Natural Numbers 
"""We can create a list of 10 natural numbers. Note:- The index of the list starts from zero"""


# Creating a List 
"""A list is created by placing the items inside [] brackets seperated by commas"""

#for example

#EXAMPLE-1
Numbers=[1,2,3,4,5,6,7,8,9,10]

print(Numbers)

#EXAMPLE-2  AN EMPTY LIST 
List1=[]

print(List1)

#EXAMPLE -3 A LIST WITH DUPLICATE ITEMS

Numbers=[1,1,1,3,4,5,4,3]
print(Numbers)

#EXAMPLE-4 A LIST WITH DIFFERENT TYPES OF ITEMS

List2=["HELLO",1,2.34,3.4,5,50,'NO']
print(List2)


#Features of a List

"""1.A list can have duplicate items"""
"""2.Items in a list are mutable"""
"""3.List can store items of different types."""


# Accessing Elements of a single dimensional List

"""A single dimensional list is a list where elements are listed one after the other"""
"""Each element is alloted a unique number called as Index"""


# EXAMPLE - A list containing multiples of 5 upto 20

my_list=[5,10,15,20]

# The index of the list is 0 for 5 , 1 for 10 and so on
"""To access a particular element from the list , we can provide the index of that element"""

print(my_list[0]) 
print(my_list[1])
print(my_list[2])
print(my_list[3])


#Negative Indexing 
"""Accessing elements from the last"""
"""In the previous list the index of 20 was 3 which can also have a negative index of -1 and so on for the other elements"""

print(my_list[-1])
print(my_list[-2])
print(my_list[-3])
print(my_list[-4])


# Accesing Elements of a Multi-Dimensional List

"""A multidimensional list is a list containing another list"""

"""For example"""
my_list2=[1,[1,2,3],'Hello',["a","b"]]

print(my_list2[0])
print(my_list2[1])
print(my_list2[2])
print(my_list2[3])

"""Not lets access the individual elements of the list which is inside mylist2"""
print(my_list2[1][0])
print(my_list2[1][1])
print(my_list2[1][2])
print(my_list2[3][0])
print(my_list2[3][1])




