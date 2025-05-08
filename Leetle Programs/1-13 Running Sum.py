def solve(nums):
    sums = []
    sum = 0
    for item in nums:
        sum += item
        sums.append(sum)
    return sums