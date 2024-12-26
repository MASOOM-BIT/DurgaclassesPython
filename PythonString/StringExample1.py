#input : B4A1D3
#output : BAD413

InputString = input("Enter String : ")
PartialString1 = PartialString2 = ''
for x in InputString:
    if x.isalpha():
        PartialString1=PartialString1+x
    else:
        PartialString2=PartialString2+x
OutputString=''
for x in sorted(PartialString1):
    OutputString=OutputString+x
for x in sorted(PartialString2):
    OutputString=OutputString+x
print('Output String',OutputString)