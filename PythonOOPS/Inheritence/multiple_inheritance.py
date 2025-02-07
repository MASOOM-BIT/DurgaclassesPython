#From multiple parents to one child
#Syntax:

class Father:
    def height(self):
        print("height is 5 feet")

class Mother:
    def color(self):
        print("Brown Color")

class child(Father,Mother):pass

c=child()
print('Child Inherited from Parents')

c.height()
c.color()

#To resolve the multiple inheritance problem : When same method is available in both Father and Mother 

class P1:
    def m1(self):
        print('P1 Method')

class P2:
    def m1(self):
        print('P2 method')

class C(P1,P2):
    pass

c=C()
c.m1() #While declaring Parents in which order you specify P1,P2 , then P1 will be consider if not then p2 will be considered