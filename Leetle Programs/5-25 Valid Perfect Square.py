def solve(num):
    n = 0
    while n ** 2 <= num:
        if n ** 2 == num:
            return True
        n += 1
    return False