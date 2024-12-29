#Append
li=[]
li.append(10)
li.append(20)
li.append(30)
li.append(40)
print(li)
#Append Example
li1=[]
for x in range(101):
    if x%10==0:
        li1.append(x)
print(li1)

#Insert : Add Element to a Specified position and other elements move to next index
#Syntax :listVariable.insert(index,element)

li2=[]
li2.append(10)
li2.append(20)
print(li2)
li2.insert(1,50)
print(li2)
li2.insert(50,77) #maximun possible value in 0,1,2 . thus it will add in the end
print(li2)
li2.insert(-10,999) #same , it will add to beginning
print(li2)

# Extend : Extending list with another list ,tuple , string set
#syntax : List1=extend(List2)

li1.extend(li2)
print(li1)

li1.extend('durga')
print(li1)

#Remove Function : (No Return) : Specified elements will be removed and index will be readjusted
li1.remove(100)
print(li1)
try:
    li1.remove('xxxx')# will give ValueError if Remove element not present in the list
except ValueError as msg:
    print(msg)

#pop() : To remove /return the Last Inserted Element in the list

print(li1.pop())
print(li1.pop())
print(li1)
li3=[]
try:
    print(li3.pop()) # if list is emplty any we try to pop , it will give index error (Thus check before pop)
except IndexError as msg:
    print(msg)

#pop(index) : To remove specific element according to a index and readjust the list and return the pop element

print(li1.pop(3))
print(li1)

try:
    print(li1.pop(100)) #give index error of error is not in the list
except IndexError as msg:
    print(msg)

# clear : Truncate the list
li1.clear()
print(li1)





