def solve(height):
    return 0 if height == [] else max([max([0] + [(j - i) * (min(height[i], height[j])) for j in range(i + 1, len(height))])] for i in range(len(height)))[0]