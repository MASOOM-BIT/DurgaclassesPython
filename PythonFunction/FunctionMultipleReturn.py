def calc(a,b):
    sum = a+b
    sub = a-b
    mul = a*b
    div = a/b
    return sum,sub,mul,div

RecivingTuple = calc(100,5) #packing

print(type(RecivingTuple))
print("The Addition : ",RecivingTuple[0])
print("The Subtraction : ",RecivingTuple[1])
print("The Multiplication : ",RecivingTuple[2])
print("The Division : ",RecivingTuple[3])