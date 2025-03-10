# report.py
#
# Exercise 2.4
import csv
import sys

def read_portfolio(filename):
    file = open(filename)
    contents = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                contents.append((row[0], int(row[1]), float(row[2])))
            except ValueError:
                print("Couldn't parse: ", row)
                next

    return contents

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

list = read_portfolio(filename)
print(list)
