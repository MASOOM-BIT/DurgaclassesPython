'''
> Properties of the File Object

> f.name -> name of File
> f.mode -> mode of File
> f.closed -> True or False to check the file
> f.readable() -> Is it read File
> f.writeable() -> or it write File
'''

f = open('abc.txt' , 'w')
print("File Name : ",f.name)
print("File Mode : ",f.mode)
print("File Readble : ",f.readable())
print("File Writeable : ",f.writable())
print("File closed : ",f.closed)


