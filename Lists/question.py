animals=['lion','tiger','monkey','elephant','frog']

filtered_animal=[]
for animal in animals:
     filtered_animal.append(animal.title())

print(filtered_animal)



#using list comprehension 

animals = ['lion', 'tiger', 'monkey', 'elephant', 'frog']
filtered_animals = [animal.title() for animal in animals]

print(filtered_animals)


# Access Nested List items by Index
L=['a','b',['cc','dd',['eee','fff']],'g','h']
print(L[2])
print(L[2][2])
print(L[2][2][0])


#Change Nested List Item value
L=['a',['bb','cc'],'d']
L[1][1]=0
print(L)

# remove items from a nested list
L=['a',['bb','cc','dd'],'e']
x=L[1].pop(1)
print(L)
print(x)

N=['a',['a','1'],['b','2']]
x=N[1].pop(1)
print(N)
print(x)


List1 = ['a']
List2 = ['b']
List2 = List1

print(List1)  
print(List2) 

List1.append('c')
print(List1) 
print(List2)  