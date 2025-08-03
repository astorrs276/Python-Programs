def solve(nums, target):
    used = set()
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if i not in used and j not in used and nums[i] + nums[j] == target:
                count += 1
                used.add(i)
                used.add(j)
    return count