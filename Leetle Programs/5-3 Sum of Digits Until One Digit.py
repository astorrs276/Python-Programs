def solve(num):
    while num // 10 != 0:
        num = sum([int(char) for char in str(num)])
    return num