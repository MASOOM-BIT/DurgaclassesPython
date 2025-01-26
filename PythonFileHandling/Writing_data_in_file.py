'''
> Use the open() function to create or open a file. Always specify the mode you want to use.

> The write() method writes a string to the file, while writelines() can be used to write a list of strings.
> f.write(str)
> f.writelines(list_of_lines)

'''
f = open('RESOURCES/abcd.txt','w')
f.write('durga\n')
f.write('Software\n')
f.write('Solution\n')
print("Data Written")

f = open('RESOURCES/abcde.txt','w')
list = ['sunny\n','bunny\n','chinny\n']
f.writelines(list)
print("Data written")
f.close()

