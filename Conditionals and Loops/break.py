# The Break Statement - used to terminate the running loops 
 
numbers=list(range(0,100))

# EXAMPLE-1
for number in numbers: 
     if number>50:
          break
     print(number,end= " ")

# EXAMPLE-2
while True:
     num=input("Enter the number (q for quit)")
     if num=='q':
         break
     print(num)
