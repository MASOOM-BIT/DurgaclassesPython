#Tell methods
#tell() methods tells the current position of the cursor in the file
#default is 0
#tell(file_pointer)
#seek() method is used to change the position of the cursor in the file
#seek(offset, from_where)

file = open("RESOURCES/file_methods.txt", "r")
print(file.tell())
print(file.read(4))
print(file.tell())
print(file.read(4))
print(file.tell())

file.seek(0)
print(file.tell())
print(file.read(4))
print(file.tell())