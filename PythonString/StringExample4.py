#CASE1
#input : RAVI  |  TEJA
#output : RTAEVJIA
from pycparser.c_ast import While

InputString1=input("Enter First String : ")
InputString2=input("Enter Second String : ")
'''
output=''
i=j=0
while i<len(InputString1) or j<len(InputString1):
    output=output+InputString1[i]+InputString2[j]
    i=i+1
    j=j+1
print(output)
'''
#CASE2
#input : RAVISOFT | TEJA
#output : RTAEVJIASOFT
output=''
i=j=0
while i<len(InputString1) or j<len(InputString2):
    if i<len(InputString1):
        output=output+InputString1[i]
        i=i+1
    if j<len(InputString2):
        output=output+InputString2[j]
        j=j+1

print(output)


