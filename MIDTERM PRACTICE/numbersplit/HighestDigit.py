def hightestdigit(num):
    if num < 10:
        return num
    else:
        return max(num % 10, hightestdigit(num // 10))
print((hightestdigit(379)))
print((hightestdigit(2)))
print((hightestdigit(377401)))