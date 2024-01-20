# FOR LOOP VS WHILE LOOP
# for loop needs an iterable object to iterate 
# while loop executes based on some condition
# for loop is used when the number of iterations is known in advance 
# while loop is used when the number of iterations is not knowon in advance 
# Both for and while loop can run infinite times

# SYNTAX FOR LOOP
# for var in iterable: 
          #do something
          
#SYNTAX FOR WHILE LOOP
# for while condition 
          #do something 
           

# EXAMPLE FOR LOOP
for i in range(1,6):
     print(i)
     
# EXAMPLE WHILE LOOP
while True:
     n=input("Enter the number ")
     if n=='q':
          break
     print(n)
      
# EXAMPLE FOR INFINITE LOOP
items=[0]
for item in items:
     print(item)
     items.append(item)


#EXAMPLE OF INFINITE WHILE LOOP
item=0
while True:
     print(item)
