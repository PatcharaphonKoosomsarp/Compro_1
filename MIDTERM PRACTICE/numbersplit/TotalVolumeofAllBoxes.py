def totalVolume(num):
    if len(num) == 0:
        return 0
    else:
        return num[0][0] * num[0][1] * num[0][2] + totalVolume(num[1:])
print(totalVolume([[4, 2, 4], [3, 3, 3], [1, 1, 2], [2, 1, 1]]))
print(totalVolume([[2, 2, 2], [2, 1, 1]]))
print(totalVolume([[1, 1, 1]]))
