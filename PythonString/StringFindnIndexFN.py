'''
#find and rfind
MainString = 'durgasoftdurgasoft'
print(MainString.find('soft')) # returns 5 as its first occur on index 5
print(MainString.find('zeenu')) # return -1 as string not found
print(MainString.rfind('soft')) # return 14 form ends
print(MainString.rfind('zen')) #rfind also return -1 if not found
print(MainString.find('soft',10,18)) #find searching for soft index 10 to 18
print(MainString.find('zen',10,18)) # return -1 if not found

# index and rindex
print(MainString.index('soft')) # returns 5 as its first occur on index 5
#print(MainString.index('zeenu')) # return ValueError  as string not found
print(MainString.rindex('soft')) # return 14 form ends
#print(MainString.rindex('zen')) #rindex also return ValueError if not found
print(MainString.index('soft',10,18)) #find searching for soft index 10 to 18
#print(MainString.index('zen',10,18)) # return ValueError if not found

#handling ValueError in index search

MainStringInput=input('Enter main String :')
SubString=input('Enter substring to search : ')
try:
    n=MainStringInput.index(SubString)
except ValueError:
    print('Value Not Found in the Main String')
else:
    print('Substring found at : ',n)
'''


#Dispaly all position of substring in the main string
MainStringInput=input('Enter main String :')
SubString=input('Enter substring to search : ')
flag=False
pos=-1
count=0
n=len(MainStringInput)
while True:
    pos=MainStringInput.find(SubString,pos+1,n)
    if pos==-1:
        break
    print('Found at index: ',pos)
    flag=True
    count=count+1
if flag==False:
    print('String Not Found')
print('occurrence',count)



