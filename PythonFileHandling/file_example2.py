# to print the no of lines in file .words,character present in tje given file
import os,sys
file_name = input("Enter the file name: ")
if os.path.exists(file_name):
    print("File exists",file_name)
    f = open(file_name, 'r')
else:
    print("File does not exist",file_name)
    sys.exit(0)

lines_count = 0
words_count = 0
characters_count = 0
for line in f:
    lines_count = lines_count+1
    characters_count = characters_count + len(line)
    words= line.split()
    print(type(words))
    words_count = words_count + len(words)
print("No of lines: ",lines_count)
print("No of words: ",words_count)
print("No of characters: ",characters_count)

