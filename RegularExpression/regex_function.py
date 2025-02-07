#1.Compile() Function:
#To find the pattern by creating asa object (regex object)

import re
pattern=re.compile('Python')
print(type(pattern))

#2.Finditer(): returns n iterator object , i.e. how many matches found
import re
pattern=re.compile('Python')
matcher=pattern.finditer('Learning Python is very easy')
print(matcher) 

#3. start() : start index of the match

#4. end() : end+1 index of match
# 5.group() : Return matched string

#example 1:
count=0
pattern2=re.compile('ab')
matcher2=pattern2.finditer('abaababa')
for match in matcher2:
    print('Match is available at start index:',match.start())
    count=count+1

print('No of Occurrence',count)
