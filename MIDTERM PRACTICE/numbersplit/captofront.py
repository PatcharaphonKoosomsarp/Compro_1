def capToFront(word):
    upper = ''
    lower = ''
    for i in word:
        if i.isupper():
            upper += i
        else:
            lower += i
    return upper + lower    
print(capToFront('hApPy'))
print(capToFront('moveMENT'))
print(capToFront('shOrtCAKE'))