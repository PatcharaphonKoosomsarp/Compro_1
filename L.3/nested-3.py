print('1-100')
columns = int(input('How many columns? '))
number = 1
while number <= 100:
    for column in range(columns):
        print(number, end='\t')
        number += 1
        if number > 100:
            break
    print('')