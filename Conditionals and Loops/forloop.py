# Introduction to the range function - It returns a series of numbers 
# syntax: Range(start,stop,step) - start here represents the starting position of the sequence. Default value is 0.
# Stop represents the stopping position fo the range() function. The number isn't inclueded in the fucntion 
# for example if we have provide the stopping position to be 5 then the number 5 isn't included in the result of the range function
# Step value represents the increment value which is by default 1.


# FOR LOOP WITH RANGE(STOP) FUNCTION - generates a sequence of integers from zero to 'STOP-1'
# for example
for i in range(5):
     print(i)

# FOR LOOP WITH RANGE(START,STOP) - generates a sequence of integers from 'START' to 'STOP-1'
# for example
for i in range(1,6):
     print(i)
print('Done!')

# FOR LOOP WITH RANGE (START,STOP,STEP)
for i in range(1,10,2):
      print(i)


# POINTS TO REMEMBER 
 
# 1.The range() function only works with integer arguemenets
# 2. All the three arguements can be positive or negative 
# 3. The step value cannot be zero.
