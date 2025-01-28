def solve(n):
    newNum = 0
    negative = False
    if n < 0:
        negative = True
        n = -n
    while n != 0:
        newNum = newNum * 10 + n % 10
        n = n // 10
    if negative:
        newNum = -newNum
    if newNum < -2**31:
        return 0
    elif newNum > 2**31:
        return 0
    return newNum