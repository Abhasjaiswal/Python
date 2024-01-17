# Accessing Characters of a String - for loop can be used to access all characters of a string 
 
# for example
name="John"

for c in name:
     print(c,end=" ")


# iterating a string in reverse order 
name="John"
for c in name[ : :-1]:
     print(c, end=" ")

     

# Accesing words of a string - split() fucntion can be used to split the string into words


sentence= "I am a good person"

count=0
for word in sentence.split():
      count+=1
      
print(f"There are {count} words in the sentence")
