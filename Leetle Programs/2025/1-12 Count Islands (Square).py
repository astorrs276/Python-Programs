def solve(grid):
    land = []
    islands = 0
    for i, line in enumerate(grid):
        for j, space in enumerate(line):
            if space == 1:
                land.append((i, j))
                try:
                    if (i - 1, j) in land:
                        continue
                except:
                    pass
                try:
                    if (i, j - 1) in land:
                        continue
                except:
                    pass
                islands += 1
    return islands