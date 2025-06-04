def solve(n):
    return int(str(n)[::-1]) if n > 0 and int(str(n)[::-1]) <= 2 ** 31 - 1 else 0 if n > 31 else -int(str(-n)[::-1]) if -int(str(-n)[::-1]) >= -2 ** 31 else 0