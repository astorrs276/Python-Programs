def solve(nums, n):
    a = nums[:n]
    b = nums[len(nums) - n:]
    c = []
    for i in range(n):
        c.append(a[i])
        c.append(b[i])
    return c