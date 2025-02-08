# > \s -> search for space character
# > \S -> Search everything except pace character
# > \d -> [0-9] search for any digit
# > \D -> [^0-9] search any digit
# > \w -> any word character i.e. alphanumeric
# > \W -> any character except word character i.e. special character
# > . -> Every character

import re
matcher = re.finditer(r'\s','a7b@ k9z')
for m in matcher:
    print('At Index',m.start(),'-->','Found Symbol',m.group())
print('---------------------------------')

matcher = re.finditer(r'\S','a7b@ k9z')
for m in matcher:
    print('At Index',m.start(),'-->','Found Symbol',m.group())
print('---------------------------------')

matcher = re.finditer(r'\d','a7b@ k9z')
for m in matcher:
    print('At Index',m.start(),'-->','Found Symbol',m.group())
print('---------------------------------')

matcher = re.finditer(r'\D','a7b@ k9z')
for m in matcher:
    print('At Index',m.start(),'-->','Found Symbol',m.group())
print('---------------------------------')

matcher = re.finditer(r'\w','a7b@ k9z')
for m in matcher:
    print('At Index',m.start(),'-->','Found Symbol',m.group())
print('---------------------------------')

matcher = re.finditer(r'\W','a7b@ k9z')
for m in matcher:
    print('At Index',m.start(),'-->','Found Symbol',m.group())
print('---------------------------------')

matcher = re.finditer(r'.','a7b@ k9z')
for m in matcher:
    print('At Index',m.start(),'-->','Found Symbol',m.group())
print('---------------------------------')