# Introduction to Infinite While Loop - A while loop can run infinitely if the condition never becomes false 

# for example

#n=100
#while True:
#     print(n)
#     n-=1



# Breaking the infinite while loop
 
while True:
     line=input("Enter the line or type q to quit")
     if line=='q':
          break
     print(line)
