stack=[1,2,3,4,5,6]
print("Original Stack is: ",stack)
stack.append(7)
print("Stack after push operation is: ",stack)
stack.pop()
print("Stack after pop operatio is: ",stack)
last_element_index=len(stack)-1
print("Value obtained after peep operation is: ",stack[last_element_index])
