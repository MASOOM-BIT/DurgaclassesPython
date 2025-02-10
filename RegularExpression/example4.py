#durgaadvjava@gmail.com

import re
s=input('Enter your mail to Validate: ')
m=re.fullmatch(r'\w[a-zA-Z0-9_.]*@gmail[.]com',s)
if m!=None:
    print('Valid Email')
else:
    print("Invalid Email")