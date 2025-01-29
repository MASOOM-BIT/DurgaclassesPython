#Python provide in built module called os module to interact with the operating system.

#Example 1: Get the current working directory
import os
cwd = os.getcwd()
print('CWD: Currect Working Directry: ',cwd)

#Example 2: To Create a sub_directry in CWD
#sub_cwd = os.mkdir('PythonDir/SubDir')
#print('Sub Directry created successfully',sub_cwd)

#Example 3 : TO create multiple sub_directry in CWD
#mul_sub_cwd = os.makedirs('SubDir1/SubDir2/SubDir2')

#To remove a directory
#os.rmdir('SubDir1/SubDir2/SubDir2')
# To remove all direcrory
# os.removedirs(path)

# To rename a directory
#os.rename('PythonDir/SubDir','PythonDir/SubDirectory')

#To Know list of content in the directory

os.listdir('PythonDir')

#to List content of directory and sub_directory
for dirpath,dirnames,filenames in os.walk('PythonDir'):
    print('Current Path:',dirpath)
    print('Directories:',dirnames)
    print('Files:',filenames)
    print()