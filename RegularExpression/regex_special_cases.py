#^ ->> start with 
#$ ->> ends with
import re
s='Learning python is hard!'
res = re.search('^Learn',s)
if res!=None:
    print('String is start with Learn')
else:
    print('String not start with Learn')

s='Learning python is hard'
res = re.search('hard$',s)
if res!=None:
    print('String is end with Hard')
else:
    print('String not end with Hard')

# To above cases to ignore Uppercase or lowercase
# re.IGNORECASE
s='Learning python is HARD'
res = re.search('hard$',s,re.IGNORECASE)
if res!=None:
    print('String is end with Hard')
else:
    print('String not end with Hard')
