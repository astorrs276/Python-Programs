def solve(s, t):
    if len(s) != len(t):
        return False
    map = dict()
    mapped = set()
    for i in range(len(s)):
        if s[i] not in map and t[i] not in mapped:
            map[s[i]] = t[i]
            mapped.add(t[i])
        elif s[i] in map and t[i] in mapped:
            if map[s[i]] != t[i]:
                return False
        else:
            return False
    return True