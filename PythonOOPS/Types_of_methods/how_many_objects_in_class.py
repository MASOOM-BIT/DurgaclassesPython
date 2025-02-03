class Test:
    count=0 #-> class/static Variable
    def __init__(self):
        Test.count=Test.count+1
    @classmethod
    def NoOfObjects(cls):
        print('The no of Object created:',cls.count)

t1=Test()
t2=Test()
Test.NoOfObjects()
t3=Test()
t4=Test()
t5=Test()
t5.NoOfObjects()