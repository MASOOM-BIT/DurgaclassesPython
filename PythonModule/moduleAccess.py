import moduleCreation

print(moduleCreation.variable_x) #Aceeessing variable_x from moduleCreation
print(moduleCreation.variable_y) #Aceeessing variable_y from moduleCreation

moduleCreation.add(10, 20) #Aceeessing add() from moduleCreation
moduleCreation.sub(10, 20) #Aceeessing sub() from moduleCreation
moduleCreation.mul(10, 20) #Aceeessing mul() from moduleCreation
moduleCreation.div(10, 20) #Aceeessing div() from moduleCreation
moduleCreation.mod(10, 20) #Aceeessing mod() from moduleCreation
moduleCreation.power(10, 20) #Aceeessing power() from moduleCreation
moduleCreation.floor_div(10, 20) #Aceeessing floor_div() from moduleCreation

'''Advantages of using modules:
1. Reusability: We can use the same module in different programs.
2. Maintainability: If we want to modify the code, we can do it in the module itself.
3. Readability: The code looks more readable when we use modules.
4. Easy to debug: If there is an error in the code, we can easily identify it by using modules.'''

#------------------------------------------------------------------------------------------

#Accessing functions and variables from a module:
#1. Directly import the module and access the functions and variables 
# using the module name as seen in above example.

#2. Import the module using an alias name:
print("------------Import the module using an alias name-------------")
import moduleCreation as mc
print(mc.variable_x) #Aceeessing variable_x from moduleCreation
print(mc.variable_y) #Aceeessing variable_y from moduleCreation

mc.add(10, 20) #Aceeessing add() from moduleCreation
mc.sub(10, 20) #Aceeessing sub() from moduleCreation
mc.mul(10, 20) #Aceeessing mul() from moduleCreation
mc.div(10, 20) #Aceeessing div() from moduleCreation
mc.mod(10, 20) #Aceeessing mod() from moduleCreation
mc.power(10, 20) #Aceeessing power() from moduleCreation
mc.floor_div(10, 20) #Aceeessing floor_div() from moduleCreation

#3. Import specific functions and variables from a module:
print("------------Import specific functions and variables from a module-------------")

from moduleCreation import variable_x, variable_y, add, sub, mul, div, mod, power, floor_div

print(variable_x) #Aceeessing variable_x from moduleCreation
print(variable_y) #Aceeessing variable_y from moduleCreation

add(10, 20) #Aceeessing add() from moduleCreation
sub(10, 20) #Aceeessing sub() from moduleCreation
mul(10, 20) #Aceeessing mul() from moduleCreation
div(10, 20) #Aceeessing div() from moduleCreation
mod(10, 20) #Aceeessing mod() from moduleCreation
power(10, 20) #Aceeessing power() from moduleCreation
floor_div(10, 20) #Aceeessing floor_div() from moduleCreation

#4. Import all functions and variables from a module:
print("------------Import all functions and variables from a module-------------")

from moduleCreation import *

print(variable_x) #Aceeessing variable_x from moduleCreation
print(variable_y) #Aceeessing variable_y from moduleCreation

add(10, 20) #Aceeessing add() from moduleCreation
sub(10, 20) #Aceeessing sub() from moduleCreation
mul(10, 20) #Aceeessing mul() from moduleCreation
div(10, 20) #Aceeessing div() from moduleCreation
mod(10, 20) #Aceeessing mod() from moduleCreation
power(10, 20) #Aceeessing power() from moduleCreation
floor_div(20, 10) #Aceeessing floor_div() from moduleCreation

#5.We can also create alias names for functions and variables while importing them from a module.

print("------------Creating alias names for functions and variables-------------")

from moduleCreation import variable_x as x, variable_y as y, add as a, sub as s, mul as m, div as d, mod as mo, power as p, floor_div as fd

print(x) #Aceeessing variable_x from moduleCreation
print(y) #Aceeessing variable_y from moduleCreation

a(10, 20) #Aceeessing add() from moduleCreation
s(10, 20) #Aceeessing sub() from moduleCreation
m(10, 20) #Aceeessing mul() from moduleCreation
d(10, 20) #Aceeessing div() from moduleCreation
mo(10, 20) #Aceeessing mod() from moduleCreation
p(10, 20) #Aceeessing power() from moduleCreation
fd(20, 10) #Aceeessing floor_div() from moduleCreation


# Note: We can also import a module from a different directory by specifying the path of the module.

#6. We can also import multiple module at the same time.
print("------------Importing multiple modules-------------")
import moduleCreation as m,random as r
print(m.variable_x) #Aceeessing variable_x from moduleCreation
print(m.variable_y) #Aceeessing variable_y from moduleCreation

m.add(10, 20) #Aceeessing add() from moduleCreation
m.sub(10, 20) #Aceeessing sub() from moduleCreation
random_number = r.randint(1, 100)
print("Random number is: ", random_number)