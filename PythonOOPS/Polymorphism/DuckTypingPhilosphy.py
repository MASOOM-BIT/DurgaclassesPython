# Duck typing is a concept in Python and other dynamic languages where the type or class of an object is determined by its behavior (methods and properties) rather than its explicit inheritance from a particular class. The name comes from the saying, "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."

# In Python, duck typing allows for more flexible and reusable code because it focuses on what an object can do rather than what it is. This means that as long as an object implements the required methods and properties, it can be used interchangeably with other objects, regardless of their class hierarchy.

# Here is an example to illustrate duck typing in Python:
class Duck:
    def quack(self):
        print("Quack!")

    def swim(self):
        print("Swim!")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")

    def swim(self):
        print("I'm swimming like a duck!")

def in_the_pond(duck):
    duck.quack()
    duck.swim()

# Both Duck and Person objects can be used in the in_the_pond function
duck = Duck()
person = Person()

in_the_pond(duck)    # Output: Quack! Swim!
in_the_pond(person)  # Output: I'm quacking like a duck! I'm swimming like a duck!
# In this example:

# Both the Duck and Person classes have quack and swim methods.
# The in_the_pond function accepts any object that has quack and swim methods, regardless of its class.
# Both Duck and Person objects can be passed to the in_the_pond function, demonstrating the duck typing philosophy.
# Duck typing promotes code flexibility and reduces the need for strict type checking, making it easier to write generic and reusable code.