# A program to print the sum of first n natural numbers

n=int(input("Enter the value of n"))
sum = 0

for i in range(0,n+1):
     sum+=i
print(sum)
    
    
# Pattern 
for i in range (5):
      print()
      for j in range(5):
           print("*",end=' ')