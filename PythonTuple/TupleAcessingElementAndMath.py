#Acessing using index and slicing
tup1 = (10,20,304,40,50)
print(tup1[0])
print(tup1[1])
print(tup1[2])
print(tup1[3])
print(tup1[4])
try:
    print(tup1[5])
except IndexError as msg:
    print(msg)

#MathlikeOprations
tup2 = ('A','B','C')
tup3 = tup1 + tup2
print(tup3)

tup4 = tup3 * 3
print(tup4)
