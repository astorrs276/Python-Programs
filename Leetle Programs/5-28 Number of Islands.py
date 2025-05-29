def solve(grid):
    count = 0
    seen = set()
    def check(x, y):
        if grid[x][y] == 1:
            seen.add((x, y))
            check(x + 1, y)
            check(x, y + 1)
            return True
        return False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) not in seen:
                if check(i, j):
                    count += 1
    return count