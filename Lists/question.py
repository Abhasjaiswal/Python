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
