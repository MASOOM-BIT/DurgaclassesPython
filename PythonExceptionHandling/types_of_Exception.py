'''
1.PreDefined Exceptions (inbuilt Eception): ex. ValueError , TypeError etc

2.UserDefined Exception : Exception based on our programming we definde exception to handle the code

Rules : Every Exception is a class in python
        class classname (parent):
        def __init__(self,arg)
        self.msg = arg
'''
class TooYoungException(Exception):
    def __init__(self, arg):
        self.msg=arg

class TooOldException(Exception):
    def __init__(self , agr):
        self.msg=agr
        
age = int(input("Enter Age : "))
if age>60:
    raise TooOldException("You are two old to Vote")
elif age<18:
    raise TooYoungException("You are too young to vote")
else:
    print("Please Proceeds to vote")