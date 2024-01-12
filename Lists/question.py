animals=['lion','tiger','monkey','elephant','frog']

filtered_animal=[]
for animal in animals:
     filtered_animal.append(animal.title())

print(filtered_animal)



#using list comprehension syntax 

animals = ['lion', 'tiger', 'monkey', 'elephant', 'frog']
filtered_animals = [animal.title() for animal in animals]

print(filtered_animals)

