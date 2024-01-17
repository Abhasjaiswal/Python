# While loop with Else- when the while loop becomes false and the loop runs normally,then the else block will be executed 
# syntax while condition:
          #statements inside while
        #else: 
         # statements inside else block
         
# EXAMPLE - LET'S CONDSIDE A LIST OF FRUITS THAT INCLUDES FOUR TYPES OF FRUITS: APPLE,BANANA,MANGO AND STRAWBERRY. WRITE A PROGRAM TO DETERMINE WHETHER THE FRUIT ORANGE IS PRESENT IN THE LIST OR NOT 

fruits=['Apple','Banana','Mango','Strawberry']

fruits_len=len(fruits)
index=0
fruit_found=False

index = 0
fruit_found = False
fruits = ["Apple", "Banana","Grapes"]
fruits_len = len(fruits)

while index < fruits_len:
    if fruits[index] == "Orange":
        print("Orange is Available")
        fruit_found = True
        break
    index += 1

if not fruit_found:
    print("Orange is not available")


while index < fruits_len:
    if fruits[index] == "Orange":
        print("Orange is Available")
        break
    index += 1
else:
    print("Orange is not available")
