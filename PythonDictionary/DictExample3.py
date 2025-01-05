#No of each vowel occurring in the given string
InputString = input('Enter String : ')
vowels = {'A','E','I','O','U','a','e','i','o','u'}
dict1={}
for x in InputString:
    if x in vowels:
        dict1[x]=dict1.get(x,0)+1

for k,v in dict1.items():
    print(k,'Vowels Occurs',v,'times')

