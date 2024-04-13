#Python supports file handling and allows users to handle files i.e., to read and write files, along with many other file handling options, to operate on files. 
#for example
# f=open('/Users/abhasjaiswal/Desktop/Python/File-IO/file.txt','r')
# data=f.read()
# print(data)
# f.close()

file=open("file.txt","rb")
print("Positon of file pointer:",file.tell())
print(file.read(10))
print('Position of file after reading is:',file.tell())
print("Setting 3 bytes from the current position of the file pointer")
file.seek(3,1)  
print(file.read())
file.close()