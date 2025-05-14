def solve(nums):
    return sum([i for i in range(len(nums) + 1)]) - sum(nums)