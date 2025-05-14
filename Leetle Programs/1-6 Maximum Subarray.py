def solve(nums):
    return max([max([sum(nums[i:j]) for j in range(i + 1, len(nums) + 1)]) for i in range(len(nums))])