# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month = month + 1
    if principal < payment:
        month_payment = principal
        principal = 0
    else:
        month_payment = payment
        if month >= extra_payment_start_month and month <= extra_payment_end_month:
            month_payment = payment + extra_payment
        principal = principal * (1+rate/12) - month_payment
    
    total_paid = total_paid + month_payment
    #print(month, round(total_paid, 2), round(principal, 2))
    print(f'{month}\t{round(total_paid, 2)}\t{round(principal, 2)}')

print('Total paid', round(total_paid, 2))
print('Months', month)
