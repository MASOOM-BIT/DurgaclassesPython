'''
>>> self:
> Default variable which is always pointing to current object.
> In previous examples , we are using s1 to acess stdent class . But when we have to acess variable and method inside a class s1 is not avilable. If I want to access current onject inside the class we ise self.
> By using self we can access instance variable and instance method.
> self id not a keyword, we can use any name instead of self but it is recommended to use self.
> self should be first parameter in constructor and instance method.
> self is not required to call instance method.
> self is not required to call instance variable.

>>> Constructor:
> it is a special method in python.
> the name shuld be __init__.
> constructor will be executed automatically at the time of object creation.
> per object constructor will be executed only once.
> purpose: to declare and initialize instance variable.
> constructor will take atleast one argument i.e self.
> constructor is optional and if we are not providing python will provide default constructor.
'''

class Student:
    def __init__(self):
        print('Constructor Executed')
    
    def m1(self):
        print('Method Executed')

s1=Student() #Constructor Executed
s1.m1() #Method Executed
