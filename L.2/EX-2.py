hours_worked = int(input('Enter the number of hours worked: '))
hourly_pay_rate = float(input('Enter the hourly pay rate: '))

if hours_worked <= 40:
    gross_pay = hours_worked * hourly_pay_rate * 1.5
else:
    gross_pay = hours_worked * hourly_pay_rate
print('Gross pay: $', format(gross_pay, ',.2f'), sep='')