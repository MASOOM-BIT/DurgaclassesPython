#staic methods : If we are not using any instance and static variable go for static varable

class DurgaMath:
    @staticmethod
    def add(x,y):
        print(x+y)
    @staticmethod
    def product(x,y):
        print(x*y)
    @staticmethod
    def avg(x,y):
        print((x+y)/2)

DurgaMath.add(10,20)
DurgaMath.product(10,20)
DurgaMath.avg(10,20)