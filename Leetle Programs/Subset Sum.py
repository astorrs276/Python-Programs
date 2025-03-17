import itertools
def solve(nums, target):
    for i in range(len(nums) + 1):
        for combination in itertools.combinations(nums, i):
            if sum(combination) == target:
                return True
    return False