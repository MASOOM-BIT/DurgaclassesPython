#findout file is present or not ,read file name from user
import os,sys
file_name = input("Enter file name : ")
if os.path.isfile(file_name):
    print("File Exists", file_name)
    opening_file = open(file_name, "r")
else:
    print("File Not Exists", file_name)
    sys.exit(1)

print("File is present")
data=opening_file.read()
print(data)