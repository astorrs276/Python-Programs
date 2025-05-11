def solve(n):
    return sum([1 if char == "1" else 0 for char in bin(n)])