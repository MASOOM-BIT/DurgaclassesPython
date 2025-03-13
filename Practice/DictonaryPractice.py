# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

N=5
d={}
for i in range(1,N+1):
	d[i]=i*i

print(d)

# Create the first dictionary 'd1' with key-value pairs.
d1 = {'a': 100, 'b': 200}

# Create the second dictionary 'd2' with key-value pairs.
d2 = {'x': 300, 'y': 200}

d1.update(d2)
print(d1)


# Create a list 'keys' containing color names.
keys = ['red', 'green', 'blue']

# Create another list 'values' containing corresponding color codes in hexadecimal format.
values = ['#FF0000', '#008000', '#0000FF']

# Use the 'zip' function to pair each color name with its corresponding color code and create a list of tuples.
# Then, use the 'dict' constructor to convert this list of tuples into a dictionary 'color_dictionary'.
color_dictionary = dict(zip(keys, values))

# Print the resulting 'color_dictionary' containing color names as keys and their associated color codes as values.
print(color_dictionary)
