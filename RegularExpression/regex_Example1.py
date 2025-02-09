'''
Rules:
1. the allowed characters are alphabet,digit # symbol
2. first character lowercase a to k 
3. the second character should be any digit divisible by 3
4. the length of identifier should be at least 2

'''
import re
s=input("Enter identifier to check: ")
m=re.fullmatch('[a-k][0369][a-zA-Z0-9]*',s)
if m!=None:
    print('valid Identifier')
else:
    print('Invalid Identifier')