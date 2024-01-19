#Iterating over a list - for loop can be used to iterate over a list 

Cars=['BMW','Audi','Toyota']

for car in Cars:
     print(car)
     
# Iterating over a list using for loop and range()

Cars=['BMW','Audi','Toyota']
for i in range (len(Cars)):
     print(Cars[i])


# List comprehension - It can produce the result in less lines of code 

Cars=['BMW','Audi','Toyota']
[print(car) for car in Cars]
