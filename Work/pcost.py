# pcost.py
#
# Exercise 1.27
import csv

def portfolio_cost(filename):
    total_value = 0
    file = open(filename)
    rows = csv.reader(file)
    headers = next(rows)

    for row in rows:
        fields = row.split(',')
        try:
            row_total = int(fields[1]) * float(fields[2])
        except ValueError:
            print("Couldn't parse :", row.strip())
            next
        total_value = total_value + row_total
    return float(total_value)

infile = 'Data/portfolio.csv'
cost = portfolio_cost(infile)
print('Total cost:', cost)
