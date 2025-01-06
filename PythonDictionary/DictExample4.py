#student record keeping
n=int(input("Enter No of Student : "))
d={}
for x in range(n):
    name = input("Name : ")
    marks = input("Marks out of 500: ")
    roll_no = int(input("Roll No : "))
    percentage =(int(marks)/500)*100
    d[name]=(marks,roll_no,percentage)

while True:
    name = input("Enter Name to fetch Marks: ")
    student_info = d.get(name, -1)  # Get student info from dictionary

    if student_info == -1:
        print('Student is not available')
    else:
        marks, roll_no,percentage = student_info  # Unpack the tuple
        print('Name:', name, '--> | Marks:', marks, ' | Roll_No -->', roll_no,' | Percentage-->',percentage)

    option = input('Search Again [Y|N] : ')
    if option == 'N' or option == 'n':
        break

