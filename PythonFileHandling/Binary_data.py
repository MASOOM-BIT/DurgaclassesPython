# >>> Reading and Writing Binary Data
# >>> To read or write binary data with files in Python, you need to use the built-in open() function with the 'rb' or 'wb' mode.

file_open = open('RESOURCES/file_handling_in_python.jpg', 'rb')
file_copy = open('RESOURCES/copy_image.jpg', 'wb')
bytes =file_open.read()
file_copy.write(bytes)
print('Image copied successfully')