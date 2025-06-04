import itertools

def solve(s1, s2):
    return any(["".join(perm) in s2 for perm in itertools.permutations(s1, len(s1))])