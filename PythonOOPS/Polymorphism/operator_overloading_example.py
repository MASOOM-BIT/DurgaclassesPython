#overloading > and <= operator for student object

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def __gt__(self,other):
        return self.marks>other.marks
    def __ge__(self,other):
        return self.marks<=other.marks
    
s1=Student('durga',100)
s2=Student('Ravi',200)

print(s1>s2)
print(s1<=s2)

# overload * operator for Empty objects
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def __mul__(self,other):
        return self.salary*other.days
    
class Time_sheet:
    def __init__(self,name,days):
        self.name=name
        self.days=days
    
    def __mul__(self,other):
        return self.days*other.salary
    
e=Employee('durga',5000)
t=Time_sheet('Durga',35)

print(e*t)
print(t*e)
