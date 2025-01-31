class Employee:
    """This is a class to create an Employee object""" #This is a docstring
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
#printing the docstring
print(Employee.__doc__)