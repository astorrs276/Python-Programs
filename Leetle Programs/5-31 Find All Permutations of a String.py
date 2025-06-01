import itertools

def solve(s):
    return ["".join(item) for item in itertools.permutations(s)]