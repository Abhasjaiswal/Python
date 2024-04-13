class Sample:
    x, y = 10, 20
    
    def display_values(self):
        print("Value of x is", self.x)
        print("Value of y is", self.y)
        print("Value of x and y =", self.x + self.y)

s = Sample()
s.display_values()

class ABC():
    var=10
    def display(self):
        print("In class method......")
obj=ABC()

print(obj.var) 
obj.display()


class Student:
     mark1,mark2,makr3 = 45,91,71
     def process(self):
         sum=Student.mark1+Student.mark2+Student.makr3
         avg=sum/3
         print("Total marks:",sum)
         print("Average marks:",avg)
         return
s=Student()
s.process()

class Odd_Even:
    even = 0
    
    def check(self, num):
        if num % 2 == 0:
            print("Even number")
            Odd_Even.even += 1
        else:
            print("Odd number")

n = Odd_Even()
x = int(input("Enter a number: "))
n.check(x)


# The __init__() Method
class ABC:
    def __init__(self,val):
        print("In Class Method")
        self.var=val
        print("The value is: ",val)
obj=ABC(10)

class Sample:
    def __init__(self, num):
        print("Constructor of class Sample")
        self.num = num
        print("The value is:", num)

S = Sample(10)
