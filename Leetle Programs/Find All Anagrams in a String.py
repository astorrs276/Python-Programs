def solve(s, p):
    places = []
    for i in range(len(s) - len(p) + 1):
        if sorted(list(s[i:i+len(p)])) == sorted(list(p)):
            places.append(i)
    return places