def solve(n):
    return int(bin(n)[2:].zfill(32)[::-1], 2)