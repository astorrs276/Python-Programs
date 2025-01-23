def solve(s):
    broken = s.split()
    new = ""
    if len(broken) > 0:
        new = broken[0]
        broken.pop(0)
        for word in broken:
            new = word + " " + new
    return new