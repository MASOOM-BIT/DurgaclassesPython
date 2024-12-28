# 1.Using while Loop
SampleList1 = [20,40,40,44,444,4545,543,]
Counter = 0
while Counter < len(SampleList1):
    print(SampleList1[Counter],end=',')
    Counter = Counter + 1

print('\n')
#2. Using For Loops

for x in SampleList1:
    print(x,end=',')

print('\n')
# To display only even Number
for i in SampleList1:
    if i%2 == 0:
        print(i,end=',')

