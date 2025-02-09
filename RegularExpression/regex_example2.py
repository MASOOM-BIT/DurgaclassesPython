'''
Rules:
1. first digit 6 ,7,8,9
2.should be only 10 digit

'''
import re
s=int(input('Enter No to validate: '))
m=re.fullmatch('[6-9][0-9]{9}',s)
if m!=None:
    print('valid Mobile No')
else:
    print('Invalid Mobile no')