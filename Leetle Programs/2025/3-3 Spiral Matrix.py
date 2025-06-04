def solve(matrix):
    if not matrix or not matrix[0]:
        return []
    result = []
    while matrix:
        result += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop(-1))
        if matrix:
            result += matrix.pop(-1)[::-1]
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop(0))
    return result