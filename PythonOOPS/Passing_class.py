class Employee:
    def __init__(self,eno,ename,esal):
        self.Eno=eno
        self.Ename=ename
        self.Esal=esal

    def display(self):
        print('Emp No :',self.Eno)
        print('Emp Name :',self.Ename)
        print('Emp Salary :',self.Esal)

class Test:
    @staticmethod
    def modify(emp):
        emp.Esal=emp.Esal+1000
        emp.display()

e=Employee(100,'Durga',1000)
Test.modify(e)

