string = input('Enter a string:')
print('This is what I found abount that string:')
if string.isalnum():
    print('The string is alphanumeric.')
if string.isalpha():
    print('The string contains only alphabetic characters.')
if string.islower():
    print('The letters in the string are all lowercase.')
if string.isnumeric():
    print('The string contains only digits.')
if string.isupper():
    print('The letters in the string are all uppercase.')
else :
    print('')