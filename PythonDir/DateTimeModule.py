from datetime import *
import os

stats = os.stat('PythonDir/DateTimeModule.py')
print('File creation time:', datetime.fromtimestamp(stats.st_ctime))
print('File modification time:', datetime.fromtimestamp(stats.st_mtime))
print('File access time:', datetime.fromtimestamp(stats.st_atime))
print('File size:', stats.st_size, 'bytes')