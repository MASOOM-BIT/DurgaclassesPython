#WAP no of occurrence of each letter in the given string
InputString = input("Enter string/Word : ")
Dict = {}
for x in InputString:
    Dict[x] = Dict.get(x,0) + 1
for k,v in Dict.items():
    print(k,'Occurs',v,'times')
