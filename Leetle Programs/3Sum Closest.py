import itertools

def solve(nums, target):
    closestSum = float('inf')
    for item in itertools.combinations(nums, 3):
        if abs(sum(item) - target) < abs(closestSum - target):
            closestSum = sum(item)
    return closestSum