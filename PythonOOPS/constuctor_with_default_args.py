#constructor with multiple optional arguments
class Strudent:
    def __init__(self,n='',m=0):
        self.name=n
        self.marks=m
    def Display(self):
        print("Name:",self.name)
        print('Marks:',self.marks)

s1=Strudent() #Not passing any arguments
s1.Display() #Name:  Marks:  0 

s2=Strudent('Durga',100)
s2.Display() #Name: Durga Marks: 100

# Constructor with mandatory argument
class Strudent:
    def __init__(self,n,m):
        self.name=n
        self.marks=m
    def Display(self):
        print("Name:",self.name)
        print('Marks:',self.marks)

s1=Strudent('Durga',100)
s1.Display() #Name: Durga Marks: 100
try:
    s2=Strudent() #TypeError: __init__() missing 2 required positional arguments: 'n' and 'm'
except Exception as e:
    print(e)