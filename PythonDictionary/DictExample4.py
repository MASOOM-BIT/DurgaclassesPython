#student record keeping
n=int(input("Enter No of Student : "))
d={}
for x in range(n):
    name = input("Name : ")
    marks = input("Makrs : ")
    d[name]=marks

while True:
    name = input("Enter Name to fetch Marks: ")
    marks = d.get(name,-1)
    if marks==-1:
        print('Student is not available :')
    else:
        print('Name :',name,'--> Marks:',marks)

    option = input(('Search Again [Y|N] : '))
    if option == 'N' or option == 'n':
        break

print('Thank You')
