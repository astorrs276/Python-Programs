def solve(nums, k):
    vals = []
    for i in range(0, len(nums) - k + 1):
        max = float("-inf")
        for j in range(i, i + k):
            if nums[j] > max:
                max = nums[j]
        vals.append(max)
    return vals