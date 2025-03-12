# Sample String : 'w3resource'
# Expected Result : 'w3ce'

sample_string = 'W'

first_two_char = sample_string[0:2]

last_two_char = sample_string[-2:]

if len(sample_string)<=1:
	print('Empty String')
else:
	print(first_two_char+last_two_char)

