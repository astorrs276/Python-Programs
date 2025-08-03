def solve(nums):
    return None if len(set(nums)) < 2 else sorted(list(set(nums)))[-2]