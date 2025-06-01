import itertools

def solve(s):
    for i in range(len(s), 0, -1):
        for item in itertools.combinations(s, i):
            if item == item[::-1]:
                return i
    return 0