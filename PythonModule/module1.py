#import module for dirModuleFunction.py
def f1():
    if __name__ == '__main__':
        print("This is the main module")
        print("Executed when the module is run directly")
        print("the value of __name__ is:",__name__)
    else:
        print("This is the imported module from another module")
        print("Executed when the module is imported")
        print("the value of __name__ is:",__name__)

f1()