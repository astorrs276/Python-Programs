def solve(s):
    return any([(s[:i] + s[i + 1:]) == (s[:i] + s[i + 1:])[::-1] for i in range(len(s))])