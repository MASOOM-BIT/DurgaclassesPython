'''
> We can use super.m1(), super().__init__..to call super class member inside child class
> By using super() we are not allowed to called instance variable , because instance variable by default single copy is there 
>thus instance variable called using self only
> 
'''
class P:
    a=10
    def __init__(self):
        self.b=20

class C(P):
    def m1(self):
        print(super().a)
        try:
            print(super().b)
        except AttributeError as msg:
            print(msg)
        print(self.b)

c=C()
c.m1()
        
'''
>>> Inside Parent class:
> static variable
> instance variable
    > only exception in child class access
> instance methods
> class methods
> static methods
>>> Inside child class where we can use super
>1. inside instance methods : No restriction to use super
>2. Inside constructor : No restriction to use super
>3. Inside class methods : from class method of child methods we can not call parent class constructor by using super()
    > Not allowed to present class instance methods
    >class method and static methods are allowed to call
>4. inside static methods:
    >static variable not access
    >Not call parent constructor
    >Not call Parent instance methods
    > not call parent class methods
    > not call parent static methods

'''
class P:
    a=10
    def __init__(self):
        print('Constructor Parent')
    def m1(self):
        print('Parent instance methods')
    @classmethod
    def m2(cls):
        print('class methods parent')
    @staticmethod
    def m3():
        print('parent static methods')

class C(P):
    def m1(self):
        print(super().a)
        super().__init__()
        super().m1()
        super().m2()
        super().m3()

c=C()
c.m1()