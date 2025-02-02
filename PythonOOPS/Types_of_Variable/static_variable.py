'''
STATIC VARIABLE:
>
If an varable have value changes object to object then we have to declare as instance variable. For every object seprate copy will be created.
> Let say if we want to declare a variable which is common for all objects then we have to declare as static variable.
>Such type of variable have to declare at class level(outside constructor and methods) as static variable.
> Thus, Only one copy of variable will be created and shared by all objects of class.

'''

class Student:
    cname='BIT' #Static variable
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

#Accessing static variable
#1. within class by using class name
#2. outside of class by using class name (Recommanded) and object reference

s1=Student('Durga',101)
print(Student.cname) #BIT
print(s1.cname,' ',s1.name,' ',s1.rollno) #BIT   Durga   101
        

