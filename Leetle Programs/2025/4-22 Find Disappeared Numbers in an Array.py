def solve(nums):
    missing = []
    for i in range(1, len(nums) + 1):
        if i not in nums:
            missing.append(i)
    return missing