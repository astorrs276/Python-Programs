def solve(nums, k):
    return [max(nums[i:i + k]) for i in range(len(nums) - k + 1)]