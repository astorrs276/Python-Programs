import itertools

def solve(nums):
    return max([combo[0] * combo[1] * combo[2] for combo in itertools.combinations(nums, 3)])