def findBigestNum(nums):
    bigest = nums[0]
    for num in nums:
        if num > bigest:
            bigest = num
    return bigest

listnum = [4, 5, 17, 3, 2, 9]

print(findBigestNum(listnum))
print(max(listnum))
print(min(listnum))