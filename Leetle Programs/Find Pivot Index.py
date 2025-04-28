def solve(nums):
    if len(nums) == 1:
        return 0
    for i in range(len(nums) - 1):
        if sum(nums[:i]) == sum(nums[i + 1:]):
            return i
    return -1