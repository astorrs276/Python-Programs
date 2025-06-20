def solve(pattern, s):
    map = dict()
    checked = set()
    broken = s.split()
    if len(broken) != len(pattern):
        return False
    for i in range(len(broken)):
        if broken[i] in map:
            if map[broken[i]] != pattern[i]:
                return False
        else:
            if pattern[i] in checked:
                return False
            map[broken[i]] = pattern[i]
            checked.add(pattern[i])
    return True