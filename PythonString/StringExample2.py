#input : a4b3c2
#output : aaaabbbcc

InputString = input("Enter the String : ")
output = ''
for x in InputString:
    if x.isalpha():
        output=output+x
        Xalphabet=x
    else:
        output=output+Xalphabet*(int(x)-1)

print(output)