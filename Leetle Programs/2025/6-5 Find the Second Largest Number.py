def solve(nums):
    return None if len(set(nums)) < 2 else max([num if num != max(nums) else 0 for num in nums])