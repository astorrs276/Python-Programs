def solve(nums):
    vals = dict()
    for num in nums:
        if num not in vals:
            vals[num] = 0
        vals[num] += 1
    for key in vals:
        if vals[key] == 1:
            return key