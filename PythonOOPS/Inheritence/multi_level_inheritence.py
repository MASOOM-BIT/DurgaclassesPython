'''
>>> Multi-Level Inheritance
> The concept of inherting from properties from multiple classes to single class with the concept of one after another
> Grand Father -> Father -> child

'''
class GF:
    def m1(self):
        print('Grand Father method')

class F(GF):
    def m2(self):
        print('Father method')

class C(F):
    def m3(self):
        print('Child method')

c=C()
c.m1()
c.m2()
c.m3()

