class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    
    def display(self):
        print(f'Name:{self.name},Roll No:{self.roll_no},Marks:{self.marks}')

s1=Student('Durga',101,90)
s1.display()
s2=Student('Ravi',102,80)
s2.display()