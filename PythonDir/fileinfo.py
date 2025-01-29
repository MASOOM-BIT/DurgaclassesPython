'''
>>> information about fileinfo module
Fields of struct stat:

1. st_dev    : ID of the device containing the file.
2. st_ino    : Inode number (serial number for the file).
3. st_mode   : Access mode and file type for the file.
4. st_nlink  : Number of hard links to the file.
5. st_uid    : User ID of the file owner.
6. st_gid    : Group ID of the file owner.
7. st_rdev   : Device ID (if the file is a character or block special device).
8. st_size   : Total size of the file in bytes (for regular files).
9. st_atime  : Time of last access (in seconds since the epoch).
10. st_mtime : Time of last data modification (in seconds since the epoch).
11. st_ctime : Time of last status change (in seconds since the epoch).
12. st_blksize: A filesystem-specific preferred I/O block size for this object.
13. st_blocks : Number of blocks allocated for this file (typically in 512-byte units).

'''

import os
os.stat('C:\Users\HP\PycharmProjects\DurgaclassesPython\PythonFileHandling\FileHandling.txt')