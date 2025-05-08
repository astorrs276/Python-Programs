def solve(n):
    num = 1
    for i in range(n, 0, -1):
        num *= i
    return num