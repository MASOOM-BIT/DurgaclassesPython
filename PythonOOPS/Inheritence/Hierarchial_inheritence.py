#Hierarchical Inheritance
#The concept of inheriting property where one parent is present and multiple children

class P:
    def m1(self):
        print('Parent Method')

class C1(P):
    def m2(self):
        print('First Child Method')

class C2(P):
    def m3(self):
        print('Second Child Method')

c1=C1()
c1.m1()
c1.m2()

c2=C2()
c2.m1()
c2.m3()


