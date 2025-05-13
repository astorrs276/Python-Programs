def solve(nums):
    def check(pos, total, peak):
        for i in range(pos + 2, len(nums)):
            peak = check(i, total + nums[i], peak)
        return max(total, peak)
    return max(check(0, nums[0], nums[0]), check(1, nums[1], nums[1])) if len(nums) > 1 else sum(nums)