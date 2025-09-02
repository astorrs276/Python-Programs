def solve(matrix, target):
    return any([target in line for line in matrix])