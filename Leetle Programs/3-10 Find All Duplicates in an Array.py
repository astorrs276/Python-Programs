def solve(nums):
    found = []
    i = 0
    while (i < len(nums)):
        val = nums.pop(i)
        if val in nums:
            for j in range(i, len(nums)):
                if nums[j] == val:
                    nums.pop(j)
                    if val not in nums:
                        found.append(val)
                    break
    return sorted(found)