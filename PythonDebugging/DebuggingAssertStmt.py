# > It is same as print statement but if i do not want unnessary print stmt in console
'''
Syntax:
1.Simple version:

assert conditional_expression:
    if yes:
        code Continues
    if no:
        assertion Error

2. Argumented Version

assert conditional_expression , message

'''

def squareit(x):
    return x**x
assert squareit(2)==4 , '2 square is 4'
assert squareit(3)==9 , '3 square is 9'

print(squareit(2))
print(squareit(3))
print(squareit(4))