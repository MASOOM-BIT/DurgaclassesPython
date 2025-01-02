InputTuple = eval(input('Input the Tuple : '))
length = len(InputTuple)
TotalSum = 0
for x in InputTuple:
    TotalSum = TotalSum + x

print(TotalSum)
print(TotalSum/length)