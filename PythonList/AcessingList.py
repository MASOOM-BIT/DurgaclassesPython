#Acessing elements of List

SampleList = [10,20,30,40]
#using index
print(SampleList[0])
print(SampleList[1])
print(SampleList[2])
print(SampleList[3])

#Acessing Nested List using index

NestedList = [10,20,[30,40]]
print(NestedList[0])
print(NestedList[1])
print(NestedList[2])
print(NestedList[2][0])
print(NestedList[2][1])

#Acessing using Slice Operator

SliceSampleList = [10,20,30,40,50,60]
print(SliceSampleList[::2]) # jumping 2 steps
print(SliceSampleList[::-1]) #reverse the list
print(SliceSampleList[0:2])