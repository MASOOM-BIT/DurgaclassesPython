#To validate car registration
#TS07EA7777
import re
s=input('Enter the car plate No:')
m=re.fullmatch('UP[0-9]{2}[A-Z]{2}[0-9]{4}',s)
if m!=None:
    print('Valid Car Registration')
else:
    print("Invalid Car Registration")