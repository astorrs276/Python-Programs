def solve(nums):
    return all([nums[i] <= nums[i + 1] for i in range(len(nums) - 1)])