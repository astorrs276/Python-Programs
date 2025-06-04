def solve(n):
    return False if n <= 1 else all([n % i != 0 for i in range(2, n // 2 + 1)])