def solve(s):
    return "".join([s[i] for i in range(len(s)) if s[i] not in s[:i]])