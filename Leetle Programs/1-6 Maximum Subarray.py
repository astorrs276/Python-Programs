def solve(nums):
    max = float("-inf")
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            sum = 0
            for k in range(i, j):
                sum += nums[k]
            if sum > max:
                max = sum
    return max