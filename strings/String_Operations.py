#Lets dive more into string and learn more about strings 

# Accessing Individual Characters
# We can access inidividual characters in a string by indexing 
# lets say we have a string "HELLO"
string='Hello'

# to access the word 'l' we can give its index. Note:- Indexing starts from 0 and spaces are also counted as a word.

print(string[0])
print(string[1])
print(string[2])
print(string[3])
print(string[4])

# we can also access string from the last by providing negative indexing 
print(string[-1])
print(string[-2])
print(string[-3])
print(string[-4])
print(string[-5])

#Accessing substring of a string- A range of characters can be accessed using slicing

#syntax" name_of_variable[start_index:end_index]

#for example

string2='Abhas Jaiswal'

print(string2[0:2])

#this will produce output "Ab" remember we have to provide an extra index of end index that we want to access.
# Here, in our case 0:A 1:B 2:H 3:A 4:S and so on.. 
# To access 'Ab' we had to provide the index as string[0:2]


#Now lets read about concatenating two strings 
# string Concatenate Operator (+) 
# let us concatenate our already defined two strings 
print(string+string2)

#string repetetion operator(*)
# It creates multiple copies of a string

print(string*100)
#this will print the string 100 times. 

