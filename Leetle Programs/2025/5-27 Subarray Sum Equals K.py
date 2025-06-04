def solve(nums, k):
    return sum([1 if sum(nums[i:j]) == k else 0 for i in range(0, len(nums)) for j in range(i + 1, len(nums) + 1)])