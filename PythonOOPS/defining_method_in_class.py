# Defining /Creating method in a class

class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks

    def read(self):
        print("Reading")

s1=Student('Durga',101,90)
print(s1.name,s1.roll_no,s1.marks)

s2 = Student('Ravi',102,80)
print(s2.name,s2.roll_no,s2.marks)

s2.read()