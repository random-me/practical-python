# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    total_value = 0
    with open(filename, 'rt') as file:
        headers = next(file)
        for line in file:
            fields = line.split(',')
            try:
                row_total = int(fields[1]) * float(fields[2])
            except ValueError:
                print("Couldn't parse :", line.strip())
                next
            total_value = total_value + row_total
    return float(total_value)

infile = 'Data/portfolio.csv'
cost = portfolio_cost(infile)
print('Total cost:', cost)
