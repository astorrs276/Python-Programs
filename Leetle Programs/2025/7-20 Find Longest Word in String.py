def solve(s):
    return "" if s == "" else max(s.split(), key=len)