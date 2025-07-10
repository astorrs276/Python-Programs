def solve(a, b):
    return max([i if a % i == 0 and b % i == 0 else 0 for i in range(1, min(a, b) + 1)])