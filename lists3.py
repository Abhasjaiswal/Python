"""Problem with the input() method"""
# Returns input from the user as a string



#Input a list using Loops

n=int(input("Enter the number of Elements: "))
 
numbers=[]
for i in range(n):
     x=int(input("Enter the elements: "))
     numbers.append(x)
     
print(numbers)

