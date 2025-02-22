class P:
    def __init__(self):
        print('Parent Constructor')

class C(P):
    def __init__(self):
        print('child COnstructor')

c=C()
