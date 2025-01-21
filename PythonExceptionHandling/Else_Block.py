'''
> We can use with try-except-finally block
> If there is no Exception , then only else block will be executed
> else block will bw exceuted if and onyif no Exception has Occured
> Finally always going to be Executed if Exception handling ornot

try:
    risky code
except :
    will bw executed if exception in try block
Else : 
    will be executed if no exception in try block
Finally :
    will be Executed always whether exception raised or not raised , 
    handled or not handled
'''

# Example
try:
    print("Try")
except:
    print("Except")
else:
    print("Else")
finally:
    print("Finally")