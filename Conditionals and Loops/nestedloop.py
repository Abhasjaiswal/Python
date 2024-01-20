# Nested for Loop - refers to a for loop inside a for loop

List1=[1,2,3]
List2=[4,5,6]

for i in List1:
     for j in List2:
          print(i, j)
     print()
          
# Nested While Loop- It is a while loop within a while loop
List1=[1,2,3]
List2=[4,5,6]

i=0
j=0
while i<len(List1):
      while j<len(List2):
            print(List1[i],List2[j])
            j+=1
      print()
      i+=1
      