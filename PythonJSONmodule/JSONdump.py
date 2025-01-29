'''
> The following techniques will be covered in this section:

>load() # To load JSON data from a file
>loads() # To load JSON data from a string
>dump() # To write JSON data to a file
>dumps() # To write JSON data to a string
'''
import json  
# Key:value mapping  
student  = {  
"Name" : "Peter",  
"Roll_no" : "0090014",  
"Grade" : "A",  
"Age": 20,  
    "Subject": ["Computer Graphics", "Discrete Mathematics", "Data Structure"]  
}  
  
with open("RESOURCES/data.json","w") as write_file:  
    json.dump(student,write_file) 

# The json.dumps() method is used to convert a Python object into a JSON string. The json.dumps() method returns a string that contains a JSON object. The json.dumps() method has the following syntax:  
student  = {  
"Name" : "Peter",  
"Roll_no" : "0090014",  
"Grade" : "A",  
"Age": 20  
}  
b = json.dumps(student)  
  
print(b)

#Python  list conversion to JSON  Array   
print(json.dumps(['Welcome', "to", "javaTpoint"]))  
  
#Python  tuple conversion to JSON Array   
print(json.dumps(("Welcome", "to", "javaTpoint")))  
  
# Python string conversion to JSON String   
print(json.dumps("Hello"))  
  
# Python int conversion to JSON Number   
print(json.dumps(1234))  
  
# Python float conversion to JSON Number   
print(json.dumps(23.572))  
  
# Boolean conversion to their respective values   
print(json.dumps(True))  
print(json.dumps(False))  
  
# None value to null   
print(json.dumps(None))