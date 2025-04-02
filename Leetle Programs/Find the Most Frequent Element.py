def solve(arr):
    items = dict()
    for item in arr:
        if item not in items:
            items[item] = 0
        items[item] += 1
    max = 0
    maxVal = None
    for key in items:
        if items[key] > max:
            max = items[key]
            maxVal = key
    return maxVal