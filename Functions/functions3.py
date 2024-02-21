def diff (x,y):
     return x-y

a=20
b=10
operation=diff(a,b)
print(operation)

#creating a function
def my_function():
     print("Hello from a function")
my_function()
#Arguements
def my_function(fname):
     print(fname + " Refsnes")

my_function("Email")
my_function("Tobias")
my_function("Linus")

#This function expects 2 arguements, and gets 2 arguemens:

def my_function(fname,lname):
     print(fname+" "+lname)
     
my_function("Emil","Refsnes")

def func():
     for i in range(4):
          print("Hello World")
          
func()

def func(i):
     print("Hello World",i)
    
func(5+2*3)

def total(a,b):
     result=a+b
     print("Sum of",a," and ",b ,"is", result)

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
total(a,b) #function call with two arguments

def func(i):
 print("Hello World",i)
j=10
func(j)

def my_function():
     print("Hello from a function")

my_function()

num1=10 #global variable
print("Global Variable num1= ",num1)

def function(num2):
     print("In function - Local Variable num2= ",num2)
     num3= 30 #local variable 
     print("In function - Local Variable num3 = ",num3)
     
func(20)   #20 is passed as an arguement to the function 
print("num1 again= ",num1)
#Error- Local variable can't be used outside the function in which it is defined
print("num3 outside function = ",num3)
