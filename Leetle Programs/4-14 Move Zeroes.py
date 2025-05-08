def solve(nums):
    i = 0
    displace = 0
    while (i < len(nums)):
        if nums[i - displace] == 0:
            nums.pop(i - displace)
            nums.append(0)
            displace += 1
        i += 1
    return nums