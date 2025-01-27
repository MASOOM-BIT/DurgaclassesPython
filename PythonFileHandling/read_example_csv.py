import csv
read_file = open('RESOURCES/example.csv', 'r')
csv_reader = csv.reader(read_file)
data=list(csv_reader)
print(type(data))
print(data)
print(type(csv_reader))
for line in data:
    for word in line:
        print(word,'\t',end='')
    print()