from math import pi


class circle:
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return pi*(self.radius*self.radius)
    
    def perimeter(self):
        return 2*pi*self.radius
    
radius=float(input('Enter the radius to find Circle radius and Parameter : '))
c=circle(radius)
print(c.area())
print(c.perimeter())
