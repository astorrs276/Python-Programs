def solve(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    vals = [0, 1]
    while (len(vals) < n):
        vals.append(vals[-1] + vals[-2])
    return vals