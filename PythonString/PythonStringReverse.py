#to reverse a given string

TestString = input("Enter the string :")
''''
print(TestString[::-1])
print(''.join(reversed(TestString)))
for x in reversed(TestString):
    print(x,end='')
print()
Reversed_String=''
length=len(TestString)-1
while length>=0:
    Reversed_String=Reversed_String+TestString[length]
    length=length-1
print(Reversed_String)
'''
#Reverse the Word
TestStringList = TestString.split()
Result_List=[]
i=len(TestStringList)-1
while i>=0:
    Result_List.append(TestStringList[i])
    i=i-1
NewWordReversesSting=' '.join(Result_List)
print(NewWordReversesSting)

WordReverseList=[]
for x in TestStringList:
    WordReverseList.append(x[::-1])
WordReversesSting=' '.join(WordReverseList)
print(WordReversesSting)








