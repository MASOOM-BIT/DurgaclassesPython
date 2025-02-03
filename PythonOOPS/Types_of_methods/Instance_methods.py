#Objects related methods
#> Inside method body , if we are accessing instance variable, that method talk about particular object , then it declare as Instance methods.Object then it declare as Insatance methods.
#> Using self word to access instace variable inside indside method body.
#> called by using ibject reference variable.

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print('Hi',self.name)
        print('Your Marks are:',self.marks)

    def grade(self):
        if self.marks>=60:
            print('First Grade')
        elif self.marks>=50:
            print('Second Grade')
        elif self.marks>=35:
            print('Third Grade')
        else:
            print('You are Failed')

n=int(input('Enter Number of Students:'))
for i in range(n):
    name=input('Enter Name:')
    marks=int(input('Enter Marks:'))
    s=Student(name,marks)
    s.display()
    s.grade()
