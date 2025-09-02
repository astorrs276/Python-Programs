def solve(temps):
    result = []
    for i in range(len(temps)):
        if len(result) < i:
            result.append(0)
        for j in range(i, len(temps)):
            if temps[j] > temps[i]:
                result.append(j - i)
                break
    return result + [0] if len(temps) > 0 else []