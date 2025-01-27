import csv
with open("RESOURCES/example.csv",'w',newline='') as csvfile:
    writer_obj=csv.writer(csvfile)
    writer_obj.writerow(['eno','ename','esal','eaddr'])
    n=int(input("Enter number of employees:"))
    for i in range(n):
        eno=int(input("Enter employee number: "))
        ename = input("Enter employee name: ")
        esal = float(input("Enter employee salary: "))
        eaddr = input("Enter employee address: ")
        writer_obj.writerow([eno,ename,esal,eaddr])
    print("Total employees data written in cdv file")