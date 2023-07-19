print('Please select operation -')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')

select = int(input('Select operations form 1, 2, 3, 4 : '))
if select == 1:
    num1 = int(input('Enter first number : '))
    num2 = int(input('Enter second number : '))
    print(num1+num2)
elif select == 2:
    num1 = int(input('Enter first number : '))
    num2 = int(input('Enter second number :  '))
    print(num1-num2)
elif select == 3:
    num1 = int(input('Enter first number : '))
    num2 = int(input('Enter second number : '))
    print(num1*num2)
elif select == 4:
    num1 = int(input('Enter first number : '))
    num2 = int(input('Enter second number : '))
    print(num1/num2)
else:
    print('Operator Error')