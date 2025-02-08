'''
> 'a' -> exactly one 'a'
> 'a+' -> at least one 'a'
> 'a*' -> any number of a's including zero number also
> 'a?' -> at most one 'a' i.e. either one a or zero number of 'a'
> a{n} -> a{3} exactly n number of 'a'
> a{n,m} -> minimum m number of 'a' and maximum n number of 'a'
> '^a' -> it will check weather the given target string start with a or not
> 'a$' -> it will check weather the given target string ends with a ot not

'''

import re
matcher = re.finditer('a','abaabaaab')
for m in matcher:
    print('At Index',m.start(),'-->','Found Symbol',m.group())
print('---------------------------------')

matcher = re.finditer('a+','abaabaaab')
for m in matcher:
    print('At Index',m.start(),'-->','Found Symbol',m.group())
print('---------------------------------')

matcher = re.finditer('a*','abaabaaab')
for m in matcher:
    print('At Index',m.start(),'-->','Found Symbol',m.group())
print('---------------------------------')

matcher = re.finditer('a?','abaabaaab')
for m in matcher:
    print('At Index',m.start(),'-->','Found Symbol',m.group())
print('---------------------------------')

matcher = re.finditer('a{3}','abaabaaab')
for m in matcher:
    print('At Index',m.start(),'-->','Found Symbol',m.group())
print('---------------------------------')

matcher = re.finditer('a{2,3}','abaabaaab')
for m in matcher:
    print('At Index',m.start(),'-->','Found Symbol',m.group())
print('---------------------------------')

matcher = re.finditer('^a','abaabaaab')
for m in matcher:
    print('At Index',m.start(),'-->','Found Symbol',m.group())
print('---------------------------------')

matcher = re.finditer('b$','abaabaaab')
for m in matcher:
    print('At Index',m.start(),'-->','Found Symbol',m.group())
print('---------------------------------')


