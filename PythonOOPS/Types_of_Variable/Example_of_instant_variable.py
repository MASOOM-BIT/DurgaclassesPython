class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40

t1=Test()
t2=Test()

print(t1.__dict__) # {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(t2.__dict__) # {'a': 10, 'b': 20, 'c': 30, 'd': 40}

del t1.c #Deleting instance variable
print(t1.__dict__) # {'a': 10, 'b': 20, 'd': 40}
print(t2.__dict__) # {'a': 10, 'b': 20, 'c': 30, 'd': 40}

t2.c=999 #changing instance variable
print(t1.__dict__) # {'a': 10, 'b': 20, 'd': 40}
print(t2.__dict__) # {'a': 10, 'b': 20, 'c': 999, 'd': 40}

t1.e=50 #Adding instance variable
print(t1.__dict__) # {'a': 10, 'b': 20, 'd': 40, 'e': 50}
print(t2.__dict__) # {'a': 10, 'b': 20, 'c': 999, 'd': 40}

del t2.d
print(t1.__dict__) # {'a': 10, 'b': 20, 'd': 40, 'e': 50}
print(t2.__dict__) # {'a': 10, 'b': 20, 'c': 999}
