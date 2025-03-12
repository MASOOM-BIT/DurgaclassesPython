# Sample String : google.com
sample_string = 'google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
expected_string = {}

for i in sample_string:
	expected_string[i]=expected_string.get(i,0)+1

# for k,v in expected_string.items():
# 	print(k,':',v)

print(expected_string)

# output : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
