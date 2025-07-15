def solve(n):
    return 1 if n == 0 else eval("*".join([str(i) for i in range(1, n + 1)]))