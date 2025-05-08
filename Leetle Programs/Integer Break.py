def solve(n):
    if n == 2:
        return 1
    elif n == 3:
        return 2
    def check(val, prod):
        if val == 0:
            return [prod]
        prods = []
        for i in range(1, val + 1):
            prods.extend(check(val - i, prod * i))
        return prods
    nums = check(n, 1)
    return max(nums)