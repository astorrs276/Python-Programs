def solve(matrix):
    new = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new[j][len(matrix[0]) - i - 1] = matrix[i][j]
    return new