'''
>>>> Reading Data
> Use the open() function to open a file in read mode.
>You can read the entire content of a file, read line by line, or read a specific number of characters.
>>>> Methods to Read Data
> read() : Total data from the file
> read(size): Reads up to size bytes from the file. If no size is specified, it reads until EOF (end of file).
> readline(): Reads the next line from the file, including the newline character.
> readlines(): Reads all lines in a file and returns them as a list.
'''
# Example 1:
f=open('abc.txt','r')
data = f.read()
print(type(data))
print(data)

print('-----------------------------------------------------------------------------')
#Example 2:
f=open('abc.txt','r')
data = f.read(30)
print(data)
f.close()
print('-----------------------------------------------------------------------------')

# Example 3:
f=open("abc.txt",'r')
print(f.readline())
print(f.readline())
print(f.readline())
f.close()
print('-----------------------------------------------------------------------------')

#Example 4:
f=open('abcd.txt','r')
list1=f.readlines()
print(list1)
for line in list1:
    print(line,end='')
f.close()
print('-----------------------------------------------------------------------------')

