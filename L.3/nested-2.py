print('1-100')
columns = int(input('How many columns ?'))
number = 1
while columns <= 0 or columns > 100:
    print('ERROR: The number cannot be negative')
    print('or greater than 100.')
    columns = int(input('Enter the correct number: '))
while number <= 100:
    for num_columns in range(columns):
        print(number, end='\t')
        number = number + 1
        if number > 100:
            break
    print('')

   