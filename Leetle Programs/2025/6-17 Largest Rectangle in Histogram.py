def solve(heights):
    return max([max([min(heights[i:j]) * (j - i) for j in range(i + 1, len(heights) + 1)]) for i in range(len(heights))])