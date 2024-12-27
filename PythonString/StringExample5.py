#to remove Duplicates in a given string
#input : ABCABCABC
#output : ABC

InputString=input("Enter the string : ")
l=[]
for x in InputString:
    if x not in l:
        l.append(x)
output = ''.join(l)
print(output)

#Alternative

s=set(InputString)
output1=''.join(s)
print(output1)