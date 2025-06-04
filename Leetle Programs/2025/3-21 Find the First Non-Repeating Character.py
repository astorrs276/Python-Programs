def solve(s):
    for i in range(len(s)):
        if s[i] not in (s[:i] + s[i + 1:]):
            return s[i]
    return ""