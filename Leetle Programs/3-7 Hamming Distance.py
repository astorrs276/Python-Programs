def solve(x, y):
    xor = bin(x ^ y)[2:]
    count = 0
    for char in xor:
        if char == "1":
            count += 1
    return count