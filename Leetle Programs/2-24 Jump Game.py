def solve(nums):
    def check(index):
        found = False
        if index + nums[index] >= len(nums) - 1:
            return True
        for i in range(1, nums[index] + 1):
            found = check(index + i)
            if found:
                return True
        return False
    return check(0)