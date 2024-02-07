fruit1='Apple'
print(fruit1 == 'Apple')
print(fruit1!='Apple')
print(fruit1<'Apple')
print(fruit1>'Apple')
print(fruit1>='Apple')


fruit1=input('Enter the name of the first fruit: ')
fruit2=input('Enter the number of the second fruit: ')

if fruit1<fruit2:
     print(fruit1 +"comes before" + fruit2 + "in the dictionary")
elif fruit1>fruit2:
     print(fruit1 + "comes after" + fruit2 + "in the dictionary")
else:
     print(fruit1+"and"+fruit2+"are the same")
