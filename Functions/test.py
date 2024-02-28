def cube(x):
     return(x*x*x)
num=10
result=cube(num)
print("Cube of ",num,"=",result)

def display():
     print("Hello")
display("Hi")

def my_function(*kids):
     print("The youngest child is "+kids[2])
     
my_function("Emil","Tobias","Linus")