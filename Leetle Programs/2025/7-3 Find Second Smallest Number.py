def solve(nums):
    return min([val for val in set(nums) if val != min(nums)]) if len(set(nums)) > 1 else -1