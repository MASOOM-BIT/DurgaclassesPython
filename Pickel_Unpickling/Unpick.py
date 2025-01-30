import Pickel_unpickel_example as emp
import pickle

f=open('RESOURCES/emp.dat','rb')
print("Employee Details: ")
while True:
    try:
        obj=pickle.load(f)
        obj.display()
        print()
    except EOFError:
        print("All employees completed")
        break
f.close()