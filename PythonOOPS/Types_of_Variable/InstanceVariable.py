'''
>>> Instance Vaiable:
> If value of a variable is varied from object to object then it is called instance variable.
> For every object a seperate copy of instance variable will be created.
> In genral we can declare instance variable inside constructor by using self.
> We can also declare instance variable inside instance method by using self.

>>> How to access instance variable:
> Within the class by using self.
> but outside of the class by using object reference.

'''
class Student:
    '''Student class with instance variables'''
    def __init__(self,x,y,z):
        self.name=x
        self.marks=y
        self.age=z
    def Display(self):
        print('Name:',self.name)
        print('Marks:',self.marks)
        print('Age:',self.age)

s1=Student('Durga',100,48)
s1.Display() #Name: Durga Marks: 100 Age: 48
s2=Student('Ravi',200,24)
s2.Display() #Name: Ravi Marks: 200 Age: 24
s3=Student('Shiva',300,30)
s3.Display() #Name: Shiva Marks: 300 Age: 30
print(Student.__doc__)

# Changing instant variable value
'''
> If we are trying to change value in a instance variable then it will be changed only for that object.
> Remaning object will not be affected.
'''
class Test:
    def __init__(self):
        self.x=10

t1=Test()
t2=Test()
print(f'Before changing {t1.x} | {t2.x}') #Before changing 10 | 10
t1.x=888
print(f'After changing {t1.x} | {t2.x}') #After changing 888 | 10

#From outside we can also declare instance variable
# --> to example of this is in PythonOOPS/Types_of_Variable/Example_of_instant_variable.py