import itertools

def solve(nums, target):
    return any([any([sum(combination) == target for combination in itertools.combinations(nums, i)]) for i in range(len(nums) + 1)])