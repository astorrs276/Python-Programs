import itertools

def solve(nums):
    peak = 0
    for i in range(1, len(nums) + 1):
        for combo in itertools.combinations(nums, i):
            if list(combo) == sorted(combo):
                peak = max(len(set(combo)), peak)
    return peak