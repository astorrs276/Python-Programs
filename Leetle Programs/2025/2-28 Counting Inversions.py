def solve(nums):
    return sum([sum([1 if nums[j] < nums[i] else 0 for j in range(i + 1, len(nums))]) for i in range(len(nums))])