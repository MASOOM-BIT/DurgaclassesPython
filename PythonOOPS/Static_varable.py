#Static Variable: A Single copy of a variable is created and shared among all the instances of the class. Static variables are defined within a class but outside any of the class's methods. Static variables are not used as frequently as instance variables are.

class Employee:
    collage_name = "IIT Bombay"
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def display(self):
        print(f'Name:{self.name},Roll No:{self.roll_no},Marks:{self.marks},Collage Name:{Employee.collage_name}')

s1=Employee('Durga',101,90)
s1.display()
print(Employee.collage_name)