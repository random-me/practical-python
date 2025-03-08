# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    total_value = 0
    file = open(filename)
    rows = csv.reader(file)
    headers = next(rows)

    for fields in rows:
        try:
            row_total = int(fields[1]) * float(fields[2])
        except ValueError:
            print("Couldn't parse :", fields)
            next
        total_value = total_value + row_total
    return float(total_value)

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
