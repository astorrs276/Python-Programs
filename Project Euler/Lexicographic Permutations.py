import itertools

permutations = list(itertools.permutations("0123456789"))

print("".join(permutations[999999]))