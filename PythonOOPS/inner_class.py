#class inside another class
#class Outer:
    #class Inner:
#without existning one type of object , if there is no clance of existing another type of objects
#Example 1:
class Outer:
    def m1(self):
        print('Outer class method')
    
    class Inner:
        def m2(self):
            print('Inner class Method')

o=Outer()
o.m1()
Outer().m1()
#i=Inner() #invalid
i=o.Inner()
i.m2()
#or
i=Outer().Inner()
i.m2()
#or
Outer().Inner().m2()

#Example 2
class Person:
    def __init__(self):
        self.name='Durga'
        self.db=self.dob()

    def display(self):
        print('Name: ',self.name)
    class dob:
        def __init__(self):
            self.dd=28
            self.mm=5
            self.yy=1957
        def dispaly(self):
            print('DOB: ',self.dd,self.mm,self.yy)


p=Person()
p.display()
p.db.dispaly()