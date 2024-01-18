Languages=['Python','Java','C++']

Languages_len=len(Languages)
Languages_found=False
index=0

while index<Languages_len:
     if Languages[index]=='Ruby':
          print("Ruby is present in the list")
          break
     index+=1
else:
     print("Ruby is not present in the list")


# Other way to use while loop 
while index<Languages_len:
     if Languages[index]=="Ruby":
           print("Ruby is available")
           Languages_found=True
           break
     index+=1

if not Languages_found:
     print("Ruby is not present in the list")
   