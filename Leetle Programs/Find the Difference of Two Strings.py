def solve(s, t):
    j = -1
    for i in range(min(len(s), len(t))):
        print(i, j, s[i], t[i])
        if j != -1:
            if s[j] == t[i]:
                return t[j]
            else:
                return s[j]
        if s[i] != t[i]:
            j = i
    if j != -1:
        if len(s) > len(t):
            return s[j]
        else:
            return t[j]
    if len(s) > len(t):
        return s[-1]
    else:
        return t[-1]

print(solve("cat", "cast"))