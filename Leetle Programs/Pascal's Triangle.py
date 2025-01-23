def solve(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1, 1]]
    else:
        list = [[1], [1, 1]]
        for i in range(n - 2):
            list.append([1, 1])
            for j in range(len(list[-2]) - 1):
                list[-1].insert(j + 1, list[-2][j] + list[-2][j + 1])
        return list