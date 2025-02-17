def solve(height):
    max = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            val = (j - i) * (min(height[i], height[j]))
            if val > max:
                max = val
    return max