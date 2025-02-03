#> You may not know all the attributes of a class at the time of writing the class.
#> thus After creating a class you need to add properties in class.

#> If you want set value to our instance vaiable we go for setter method.
#> If you want to get value from instance variable we go for getter method.
#> It is Recommended to use getter and setter method to access the instance variable.

'''
Syntax:
s=Student()
s.setName('Durga')
print(s.getName())

def setName(self,name):
    self.name=name

def getName(self):
    return self.name
'''

class Student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks

n=int(input('No of Studens: '))
for i in range(n):
    s=Student()
    name=input('Name : ')
    s.setName(name)
    marks=int(input("Marks :"))
    s.setMarks(marks)
    print('Name: ',s.getName())
    print('Marks : ',s.getMarks())
