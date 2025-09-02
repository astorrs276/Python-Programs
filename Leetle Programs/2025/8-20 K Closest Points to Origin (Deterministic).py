def solve(k, points):
    return sorted(points, key=lambda item:((item[0] ** 2 + item[1] ** 2) ** .5, item[0], item[1]))[:k]