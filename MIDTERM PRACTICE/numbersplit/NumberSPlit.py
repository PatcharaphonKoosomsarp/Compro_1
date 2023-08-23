def numbersplit():
    num = int(input("Enter a number: "))
    half = num // 2
    return [half, num - half]
output = numbersplit()
print(output)