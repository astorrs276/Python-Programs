def solve(intervals):
    return len(set([i for item in intervals for i in range(item[0], item[1])])) == len([i for item in intervals for i in range(item[0], item[1])])