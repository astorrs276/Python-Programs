def solve(n):
    return n in [3 ** i for i in range(int(n ** 1/2) + 1)]