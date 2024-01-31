# Introduction - The else block will be executed only when the loop is NOT Terminated abruptly by the break keyword

# SYNTAX - FOR VAR IN SEQUENCE:
             #STATEMENTS INSIDE FOR
           #ELSE:
            #STATEMENTS INSIDE ELSE
            
# USE OF FOR LOOP WITH ELSE BLOCK 

Languages=['Python','Rust','C','C++']

for Lang in Languages:
      if 'Python'==Lang:
           print("I like Python")
           break
      else:
          print("I dont like Python")
 
for letter in "HELLO":
      print(letter,end=" ")
else:
      print("Done")
