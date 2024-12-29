MatrixList = [[10,20,30],[40,50,60],[70,80,90]]
print(MatrixList)
#Row Wise
for i in MatrixList:
    print(i)

#matrix wise
for i in range(len(MatrixList)):
    for j in range(len(MatrixList[i])):
        print(MatrixList[i][j],end=',')
    print()
