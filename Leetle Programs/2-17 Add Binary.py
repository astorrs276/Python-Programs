def solve(a, b):
    sum = 0
    for i in range(len(a)):
        sum += 0 if a[i] == "0" else 2**(len(a) - i - 1)
    for i in range(len(b)):
        sum += 0 if b[i] == "0" else 2**(len(b) - i - 1)
    return bin(sum)[2:]