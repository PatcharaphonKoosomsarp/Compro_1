hours_work = int(input("Enter Hours worked: "))
pay_rate = int(input("Enter hourly pay rate: "))

calculate = hours_work * pay_rate

print("Gross Pay: ", format(calculate, ',.2f'))