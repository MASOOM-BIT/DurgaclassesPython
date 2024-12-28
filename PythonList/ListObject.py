# Empty String
EmptyList=[]

#if the Element of list is Known
KnownList = [10,20,30,40,None,'Abc','ABCD','10.3',True,False] #Heterogenous Element Present
print(KnownList)
#Read Dynamically

DynamicalList = eval(input('Enter the List : '))
print(DynamicalList)

#With list() function

FunctionList1 = list(range(0,20,4))
print(FunctionList1)

String = 'Durga'
FunctionList2 = list(String)
print(FunctionList2)

#With Split Function

String2 = 'Durga Teaching Python'
SplitList = String2.split()
print(SplitList)


# Nested List

NestedList = [10,20,[30,40],[5,60]]
print(NestedList)