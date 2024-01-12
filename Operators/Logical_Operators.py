#Logical Operators 
"Used to combine expression"

#List of Logical Operators

# 1.Logical AND (and)
# 2.Logical OR (or)
# 3.Logical NOT (not)  (Note:- Logical Not is the only unary operator)

#1. Logical AND (and) - Returns true when all the statements are true, else returns false.

#For example
x=10
y=20
z=30

if x < y and y < z :
     print("True")
else:
     print("False")

# The Output will be true because x is less than y and y is less than z,as all the statements specified in the if construct are true.

# 2.Logical OR (or) - returns true if any one condition is true else returns false.

#For example
x=20
y=30
z=40

if x<y or z<x:
     print("True")
else:
     print("False")
     
# The output will be true because x is less than y but z is not less than x. since one of the condition is true out of all therefore the output will be true

# 3. Logical NOT (not) - Returns true if the conditional expression returns false, and vice versa

#for example
x=10
y=20
z=30

if not(x > y or x >z):
     print("x is not the largest number")
else:
     print("x is not the smallest number")