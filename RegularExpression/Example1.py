import re
count=0
# pattern=re.compile('ab')
# matcher=pattern.finditer('abaababa')
matcher=re.finditer('ab','abaababa')

for match in matcher:
    count=count+1
    print(match.start())
    print(match.end())
    print(match.group())

print('No of Occurrence',count)
