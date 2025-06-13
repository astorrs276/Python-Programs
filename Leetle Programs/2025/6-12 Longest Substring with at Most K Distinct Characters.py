def solve(k, s):
    return 0 if s == "" else max([max([j - i if len(set(s[i:j])) <= k else 0 for j in range(i, len(s) + 1)]) for i in range(len(s))])