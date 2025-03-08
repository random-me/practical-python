# pcost.py
#
# Exercise 1.27
infile = 'Data/portfolio.csv'
total_value = 0

with open(infile, 'rt') as file:
    headers = next(file)
    for line in file:
        fields = line.split(',')
        row_total = int(fields[1]) * float(fields[2])
        total_value = total_value + row_total

print("Total cost ", total_value)
