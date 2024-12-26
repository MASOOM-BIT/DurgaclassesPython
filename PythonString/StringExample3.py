#input : a4k3b2
#output : aeknbd
#chr(unicode)=character
#ord(character)=unicode
print(chr(97))
print(ord('a'))
InputString = input('Enter the string : ')
output = ''
for x in InputString:
    if x.isalpha():
        output=output+x
        AlphabetChar=x
    else:
        newch=chr(ord(AlphabetChar)+int(x))
        output=output+newch

print(output)