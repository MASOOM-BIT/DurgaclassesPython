# 1> [abc] -> Search for either a ,b or c
# 2> [^abc] -> Search all character except a,b,c
# 3> [a-z] -> Search for lowercase Alphabet symbol
# 4> [A-Z] -> Search for uppercase Alphabet symbol
# 5> [a-zA-Z] -> Search for any Alphabet symbol Uppercase or lowercase
# 6> [0,9] -> Number Search
# 7> [a-zA-Z0-9] -> Searching AlphaNumeric Symbol
# 8> [^a-zA-Z0-9] -> Special symbol (except Alphanumeric character)

import re
matcher = re.finditer('[abc]','a7b@k9z')
for m in matcher:
    print('At Index',m.start(),'Found Symbol',m.group())
print('---------------------------------')
import re
matcher = re.finditer('[a-z]','a7b@k9z')
for m in matcher:
    print('At Index',m.start(),'Found Symbol',m.group())

print('---------------------------------')
import re
matcher = re.finditer('[0-9]','a7b@k9z')
for m in matcher:
    print('At Index',m.start(),'Found Symbol',m.group())


print('---------------------------------')
import re
matcher = re.finditer('[^a-zA-Z0-9]','a7b@k9z')
for m in matcher:
    print('At Index',m.start(),'Found Symbol',m.group())
