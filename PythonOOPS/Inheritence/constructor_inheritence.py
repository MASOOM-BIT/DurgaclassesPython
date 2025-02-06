class P:
    a=10
    def __init__(self,x):
        self.x=x
class C(P):
    pass

c=C()
print(c.a)

#TypeError: P.__init__() missing 1 required positional argument: 'x'
#The error TypeError: P.__init__() missing 1 required positional argument: 'x' occurs because the class C inherits from class P, and class P's __init__ method requires an argument x. When you create an instance of C without providing the argument x, the __init__ method of the parent class P is implicitly called, but the required argument is missing, resulting in a TypeError.
