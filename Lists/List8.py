Languages=['Java','C++']
print(Languages)

# A list can have duplicate items
Languages=['Java','C++','C++']
print(Languages)

# Items in a list are mutable
Languages=['Java','C++','Python']
Languages[1]='c'
print(Languages)

# Acessing Elements of a single dimensional list
print(Languages[0])
print(Languages[1])
print(Languages[2])

# Methods of Inserting Elements 

#Using append Method
Languages=['Java','C++','Python']
Languages.append('Ruby')
print(Languages)

#Using insert method (For specific Index)
Languages=['Java','C++','Python']
Languages.insert(0,'JavaScript')
print(Languages)

#Using Extend Method

Languages=['Java','C++','Python']
Web_Development=['JavaScript','CSS','Rust']

Languages.extend(Web_Development)
print(Languages)

#Input a list using Loops

n=int(input("Enter the number of Elements: "))
 
numbers=[]
for i in range(n):
     x=int(input("Enter the elements: "))
     numbers.append(x)
     
print(numbers)

