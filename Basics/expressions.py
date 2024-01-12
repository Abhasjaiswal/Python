#Expressions in Python - Combination of operators and operands
 
# Constant Expressions - It has only constants as operands
#for example "10+20"

#Arithmetic Expressions - Containts numeric values or strings as operands, arithmetic operators and sometimes paranthesis

#for example
x="hello"
print(x*3) # x*3 is an arithmetic expression

#Integral Expression - Results an integer after performing neccesary type conversions 
x=5
y=7.5
res=x+int(y)
print(res)  # results an integer


#Floating point expressions - Results a floating-point value after performing necessary type conversions

x=5
y=7.5
res=float(x)+y
print(res)  # results a float point value 


#Relational Expressions - are also called as boolean expressions i.e. returns a boolean value

z=(10+3)<=(2+3)
print(z)


#Logical Expressions - cosists of relational expression connected using logical opertors and it always returns a boolean value

c=(10<13) and (2>3)
print(c)


#Bitwise Expressions - contains bitwise operators and the computations are always performed at bit level

d=10<<2
print(d)


#Combinational Expressions - combination of different expressions 
x=10
y=20
z=y+(x<<1)-x*3
print(z)



#PRECEDENCE OF OPERATORS IN PYTHON

#  OPERATORS       

#  (),[],{}                                 highest 
#     **
#    +a , -a 
#   *, / , // , %
#   + , -
#  << , >>
#    &
#    ^
#     |
#    >= <= > <
#   != , ==
#  is , is not , in , not in 
#    not 
#   and
#   or 
#   =,+=,-=,,/=,*=                           lowest 



