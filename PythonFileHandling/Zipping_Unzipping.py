'''
>>> Zipping Files

> To create a ZIP file, you can use the ZipFile class from the zipfile module. Here's how to do it:
> Import the necessary module.
> Create a ZipFile object in write mode.
> Add files to the ZIP archive using the write() method.
> Close the ZIP file to ensure all data is written.

>>> Unzipping Files
> To extract files from a ZIP archive, you can also use the ZipFile class but in read mode. You can extract all files or specific ones.
'''

# Example: Zipping Files
import zipfile
from zipfile import ZIP_DEFLATED
f=zipfile.ZipFile("RESOURCES/zipped_file.zip",'w',ZIP_DEFLATED)
f.write('RESOURCES/zipfile1.txt')
f.write('RESOURCES/zipfile2.txt')
f.write('RESOURCES/zipfile3.txt')
f.close()
print("Files Zipped Successfully")

from zipfile import ZIP_STORED
f1=zipfile.ZipFile("RESOURCES/zipped_file.zip",'r',ZIP_STORED)
names=f1.namelist()
for name in names:
    print('File Name: ',name)
    f2=open(name,'r')
    print(f2.read())
    print()