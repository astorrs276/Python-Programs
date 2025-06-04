def solve(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        seq = [1, 1]
        for i in range(2, n + 1):
            seq.append(seq[i - 1] + seq[i - 2])
        return seq[-1]