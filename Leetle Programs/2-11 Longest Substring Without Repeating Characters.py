def solve(s):
    return 0 if s == "" else max([max([j - i if len(s[i:j]) == len(set(s[i:j])) else 0 for j in range(i + 1, len(s) + 1)]) for i in range(len(s))])