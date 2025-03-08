def solve(nums, k):
    nums = nums[len(nums) - k:len(nums)] + nums[0:len(nums) - k]
    return nums