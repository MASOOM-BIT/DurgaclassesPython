#Whatever method Constructor,variable present inside parent are available to the child class.
#Sometimes child class may not satisfying with parent class implementation ,if child class not satisfy with parent class implementation, then child is allowed to override the method ,constructor and variable of parent based on ots requirement is known as overriding

class P:
    def property(self):
        print('cash+land+gold')
    
    def marry(self):
        print('Appal')

class C(P):
    def marry(self):
        print('kat')

c=C()
c.property()
c.marry()