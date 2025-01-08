#There two types of variable present in python Function
#1. Global variable
"""A variable declare outside of the function is called global variable,
which is accessible inside or outside of the function/module"""
a=10  #global variable
def f1():
    print("F1->",a)  #Output: 10 #Here, a is global variable and it is accessible inside the function f1
def f2():
    print("F2->",a)  #Output: 10 #Here, a is global variable and it is accessible inside the function f2
f1()
f2()
#2. Local variable
"""A variable declare inside of the function is 
called local variable, which is accessible only inside the function"""
def f3():
    b=20  #local variable
    print("F3->",b)  #Output: 20 #Here, b is local variable and it is accessible inside the function f3
def f4():
    print("F4->",b)  #NameError: name 'b' is not defined #Here, b is local variable and it is not accessible outside the function f4

f3()
try:
    f4()
except NameError as e:
    print(e)

# case 3 : Global variable and Local variable with same name
"""If a global variable and a local variable have the same name,
always consider the local variable inside the function"""
c=30  #global variable
def f5():
    c=40  #local variable
    print("F5->",c)  #Output: 40 #Here, c is local variable and it is accessible inside the function f5
def f6():
    print("F6->",c)  #Output: 30 #Here, c is global variable and it is accessible inside the function f6
f5()
f6()
#case 4: Global variable and Local variable with same name and using global keyword
"""If we want to use a global variable inside the function, we can use the global keyword"""
d=50  #global variable
def f7():
    global d  #using global keyword
    d=60  #changing the value of global variable
    print("F7->",d)  #Output: 60 #Here, d is global variable and it is accessible inside the function f7
def f8():
    print("F8->",d)  #Output: 60 #Here, d is global variable and it is accessible inside the function f8
f7()
f8()
#Note: global a=999 is not allowed
#global a
#a=999 is allowed only
e=20
def f9():
    e=10
    print("F9->",globals()['e'])  #Output: 10 #Here, e is local variable and it is accessible inside the function f9 using globals() function
f9()    