def find_peak_indices(nums):
    return [i for i in range(1, len(nums) - 1) if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]]

def print_peak_indices(nums, peak_indices):
    print(f"Peak element index of: {nums} -> {peak_indices}")

nums1 = [3, 2, 3, 1]
nums2 = [1, 2, 1, 3, 5, 6, 4]
nums3 = [1, 2, 1, 4, 5, 6, 4, 7]

print_peak_indices(nums1, find_peak_indices(nums1))
print_peak_indices(nums2, find_peak_indices(nums2))
print_peak_indices(nums3, find_peak_indices(nums3))
