def solve(matrix):
    return [[matrix[len(matrix) - j - 1][i] for j in range(len(matrix[i]))] for i in range(len(matrix))]