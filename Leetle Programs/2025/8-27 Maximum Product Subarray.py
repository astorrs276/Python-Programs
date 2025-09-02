import math
def solve(nums):
    return 0 if nums == [] else max([max([math.prod(nums[i:j + 1]) for j in range(i, len(nums))]) for i in range(len(nums))])