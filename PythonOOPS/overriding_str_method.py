class Student:
    def __init__(self,name,roll_no) -> None:
        self.name=name
        self.roll_no=roll_no
    def __str__(self) -> str:
        return f'Student Name: {self.name} and Roll No: {self.roll_no}'
    
    

s1=Student('Durga',101)
s2=Student('Ravi',102)
print(s1)
print(s2)
