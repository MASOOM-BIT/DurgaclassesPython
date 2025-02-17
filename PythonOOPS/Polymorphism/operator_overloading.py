#operator overloading:
# '+' operator is overload , addition,concat
# for my own customized object we can use '+' also
class Book:
    def __init__(self, pages):
        self.pages=pages

b1=Book(100)
b2=Book(200)
#print('Total Pages:',b1+b2)

# To add Functionally
# '+' every operator internally there is a method associated with that,if we overwrite that method is my book class, it add the two object reference

# Such type of method is called Magic Method

# '+' will call magic method and implement it.

# '+' -->>> __add__()

class Book:
    def __init__(self, pages):
        self.pages=pages
    
    def __add__(self,other):
        return self.pages+other.pages

b1=Book(100)
b2=Book(200)
print('Total Pages:',b1+b2)
