def solve(intervals):
    vals = []
    for item in intervals:
        for i in range(item[0], item[1] + 1):
            vals.append(i)
    vals = sorted(list(set(vals)))
    if len(vals) == 0:
        return []
    start = vals.pop(0)
    end = start + 1
    newIntervals = []
    for num in vals:
        if num != end:
            newIntervals.append([start, end - 1])
            start = num
            end = start + 1
        else:
            end += 1
    newIntervals.append([start, end - 1])
    return newIntervals