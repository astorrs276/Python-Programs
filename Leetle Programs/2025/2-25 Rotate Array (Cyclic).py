def solve(nums, k):
    return nums[len(nums) - k:len(nums)] + nums[0:len(nums) - k]