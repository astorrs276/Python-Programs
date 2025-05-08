def solve(matrix):
    newMatrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for i, line in enumerate(matrix):
        for j, char in enumerate(line):
            newMatrix[j][len(matrix[0]) - 1 - i] = char
    return newMatrix