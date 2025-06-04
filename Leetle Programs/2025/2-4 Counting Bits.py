def solve(n):
    bits = []
    for i in range(n + 1):
        ones = 0
        num = i
        vals = [1]
        while vals[-1] < num:
            vals.append(vals[-1] * 2)
        for item in sorted(vals, reverse=True):
            if item <= num:
                num -= item
                ones += 1
        bits.append(ones)
    return bits