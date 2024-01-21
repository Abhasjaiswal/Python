#Return Statement:
#Basic Function with Return:

#In Python, a function can use the return statement to send a value back to the caller.

def add_numbers(a, b):
    result = a + b
    return result

#When you call this function, it calculates the sum of a and b and gives you back the result.
sum_result = add_numbers(3, 4)
print(sum_result)  # Output: 7



# Function Completion with Return:

#When a function encounters a return statement, it stops executing further code in that function.
def check_positive_number(num):
    if num > 0:
        return "Positive"
    else:
        return "Non-positive"

result = check_positive_number(5)
print(result)  # Output: Positive



#Yield Statement:
#Basic Function with Yield:
#yield is used in the context of generator functions. A generator is a special type of iterable that is created using a function with yield.
def generate_numbers():
    yield 1
    yield 2
    yield 3
#When you call this function, it returns a generator.
my_generator = generate_numbers()


#Lazy Evaluation with Yield:
#Unlike return, yield allows a function to produce a sequence of values one at a time. It's memory-efficient for large datasets.

def generate_numbers():
    for i in range(5):
        yield i

#You can use a generator in a for loop to get values one by one.
for num in generate_numbers():
    print(num)



#Stateful Iterations with Yield:
#yield maintains the state of the function between calls. It allows the function to remember where it left off.
def counter():
    count = 0
    while True:
        yield count
        count += 1
#You can use this generator to get the next count each time you call it.
my_counter = counter()
print(next(my_counter))  # Output: 0
print(next(my_counter))  # Output: 1


#return is used for regular functions that calculate a value and complete, while yield is used in generator functions for lazy evaluation, producing a sequence of values, and maintaining stateful iterations. Generators are particularly useful when dealing with large datasets or scenarios where values are produced over time.