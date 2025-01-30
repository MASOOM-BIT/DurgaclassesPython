import Pickel_unpickel_example as emp
import pickle

f=open('RESOURCES/emp.dat','wb')
n=int(input("ENter the number of employees: "))
for i in range(n):
    eno=int(input("Enter employee number: "))
    ename=input("Enter employee name: ")
    esal=float(input("Enter employee salary: "))
    eaddr=input("Enter employee address: ")
    e=emp.Employee(eno,ename,esal,eaddr)
    pickle.dump(e,f)
f.close()
