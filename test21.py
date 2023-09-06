def find_peak_indices(nums):
    peak_indices = []

    for i in range(len(nums)):
        if i == 0 and nums[i] > nums[i + 1]:
            peak_indices.append(i)
        elif i == len(nums) - 1 and nums[i] > nums[i - 1]:
            peak_indices.append(i)
        elif nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            peak_indices.append(i)

    return peak_indices

nums1 = [3, 2, 3, 1]
nums2 = [1, 2, 1, 3, 5, 6, 4]
nums3 = [1, 2, 1, 4, 5, 6, 4, 7]

peak_indices1 = find_peak_indices(nums1)
peak_indices2 = find_peak_indices(nums2)
peak_indices3 = find_peak_indices(nums3)

print(f"Peak element index of {nums1} -> {peak_indices1}")
print(f"Peak element index of {nums2} -> {peak_indices2}")
print(f"Peak element index of {nums3} -> {peak_indices3}")
