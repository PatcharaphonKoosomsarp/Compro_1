def main():
    hours = int(input('How many hours did you work? '))

    pay_rat = float(input('What is your pay rate? '))

    gross_pay = hours * pay_rat

    print('Gross pay: $', format(gross_pay, ',.2f'), sep='')

main()