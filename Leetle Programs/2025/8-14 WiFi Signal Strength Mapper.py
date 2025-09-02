def solve(point, routers):
    return max(0, max([0] + [router[2] - ((point[0] - router[0]) ** 2 + (point[1] - router[1]) ** 2) ** .5 for router in routers]))