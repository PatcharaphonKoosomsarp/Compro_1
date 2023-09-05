def simplePair(arr, n):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] * arr[j] == n:
                return [arr[i], arr[j]]

print(simplePair([1, 2, 3], 3))
print(simplePair([1, 2, 3], 6))
print(simplePair([1, 2, 3], 9))