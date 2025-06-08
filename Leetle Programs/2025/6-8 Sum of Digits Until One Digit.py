def solve(n):
    while n >= 10:
        n = sum(int(s) for s in str(n))
    return n