def solve(nums):
    return 0 if not nums or sum(nums) == 0 else min([sum(nums[:i + 1]) for i in range(len(nums)) if sum(nums[:i + 1]) != 0])