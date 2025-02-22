#for constructor Also overloading is not allowed is not Applicable

class Test:
    def __init__(self):
        pass
    def __init__(self,a):
        pass
    def __init__(self,a,b):
        pass

t=Test()

#Error: TypeError: Missing positional argument
#each constructor override previous one will be deleted ,Thus a constructor overloading is not possible
#It can be also possible using default argument and variable number argument
