def solve(jewels, stones):
    return sum([1 if char in jewels else 0 for char in stones])