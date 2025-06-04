import math

def solve(nums):
    return [math.prod(nums[:i] + nums[i + 1:]) for i in range(len(nums))]