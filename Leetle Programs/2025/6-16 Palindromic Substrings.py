def solve(s):
    return sum([sum([1 if s[i:j] == s[i:j][::-1] else 0 for j in range(i + 1, len(s) + 1)]) for i in range(len(s))])