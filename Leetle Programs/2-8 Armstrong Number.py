def solve(num):
    original = num
    nums = []
    while num > 0:
        nums.append(num % 10)
        num //= 10
    sum = 0
    for item in nums:
        sum += item ** len(nums)
    if sum == original:
        return True
    return False