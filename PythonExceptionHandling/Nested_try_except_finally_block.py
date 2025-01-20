try:
    print("Outer try block")
    try:
        print("Inner try Block")
        print(10/0)
    except ZeroDivisionError:
        print("Inner Except block")
    finally:
        print("Inner finally blaock")
except:
    print("Outer Except block") # No error so control will never get here
finally:
    print("Outer finally block")


'''
try:
    stmt-1
    stmt-2
    stmt-3
    try:
        stmt-4
        stmt-5
        stmt-6
    except XYZ:
        stmt-7
    finally:
        stmt-8
    stmt-9
except XYYX:
    stmt-10
finally:
    stmt-11
stmt-12
'''

'''
CASE 1: No Exception
output: 1,2,3,4,5,6,8,9,11,12,Normal termination
'''

'''
CASE 2: Exception at stmt-2 ,crossponding except block match
output : 1,10,11,12 Normal Termination
NOTE : Inner finally block will not execute beceiuse we never reach to inner try block
'''
'''
CASE 3: If exception at stmt2 and crossponding except block not matched
output : 1,11 , Abnormal Termination
'''
'''
CASE 4: If Excepetion at stmt-5 and crossponding inner inner bolck matched
output : 1,2,3,4,7,8,9,11,12,Normal Terminal
'''
'''
CASE 5: If Exception occurs at stmt-5 and ....
'''

