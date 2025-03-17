import itertools
def solve(s1, s2):
    perms = itertools.permutations(s1, len(s1))
    for perm in perms:
        if "".join(perm) in s2:
            return True
    return False