def solve(num):
    return num == sum([int(char) ** len(str(num)) for char in str(num)])