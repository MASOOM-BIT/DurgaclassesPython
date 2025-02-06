'''
super():
    In child class we can access parent class members explicity by using keyword super()
    ,except Instance variable

> call instance variable in clild class by using self only
> If clild class contain instance variable and parent class contains instance variable with the same name , the most recent value variable will be there

'''
#Example 1:
class P:
    a=888
    def m1(self):
        self.a=10
class C(P):
    def __init__(self):
        print(super().a)
        print(self.a)
c=C()

#Example 2:
class P1:
    def __init__(self):
        self.b=10
    
class C1(P1):
    def __init__(self):
        super().__init__()
        self.b=20
        print(self.b)
c1=C1() #20 , most recent

#example 3:
class P3:
    def __init__(self):
        self.b=10

class C3(P3):
    def __init__(self):
        self.b=20
        super().__init__()
        print(self.b)
c3=C3() #10 , most recent