from itertools import combinations
def solve(nums):
    peak = 0
    for combo in combinations(nums, 3):
        peak = max(peak, combo[0] * combo[1] * combo[2])
    return peak