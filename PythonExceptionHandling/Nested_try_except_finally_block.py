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
CASE 5: If Exception occurs at stmt-5 and crossponding inner block not matched but outer block matched
output : 1,2,3,4,8,10,11,12 Normal Termination
NOTE : Before going to outer except block inner finally will be executed
'''

'''
CASE 7 : If Exception raised at stmt 7 and crossponding except block is matchd ,Assuming 
error occut at 4
output : 1,2,3,8,10, 12 , Normal Termination
NOTE : If there is exception at inner except it will look at outer except block for code handiling
'''

'''
CASE 8: Eception at stmt 7 (Assuming error at stmt 4) and crosponding except block not matched
output : 1,2,3,8,11 Abnormal termination
'''

'''
CASE 9 : Exception at stmt 8 and crossponding except block matched
output : 1,2,3 (4,5,6,7 may or may not) 10,11,12,Normal termination

CASE 10 : Exception at stmt 8 and crossponding except block not matched
output  : 1,2,3, (4,5,6,7 may or may not) ,11,abnormal termination

CASE 11 : Exception at stmt 9 and crossponding except bloack matched
output : 1,2,3,(4,5,6,7 may or may not) 8,10,11,12 Normal termination

CASE 12 : Exception at stmt 9 and crossponding except blaock is not matched
Output : 1,2,3 (4,5,6,7 may or may not) 8,11 , Abnormal termination

Case 13 : Exception at stmt 10 
output : ....11, Abnormal termination

CASE 14 : Exception at stmt 11 ot stmt -12
Abnormal termination
'''


