def solve(binary):
    return sum([int(binary[i]) * (2 ** (len(binary) - i - 1)) for i in range(len(binary))])