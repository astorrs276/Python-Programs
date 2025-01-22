def pascal(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1, 1]]
    else:
        triangle = [[1], [1, 1]]
        for i in range(n - 2):
            triangle.append([1, 1])
            for j in range(len(triangle[-2]) - 1):
                triangle[-1].insert(j + 1, triangle[-2][j] + triangle[-2][j + 1])
        return triangle
