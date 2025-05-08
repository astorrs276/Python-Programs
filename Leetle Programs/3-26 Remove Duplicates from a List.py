def solve(arr):
    i = 0
    while i < len(arr):
        val = arr.pop(i)
        if not val in arr[:i]:
            arr.insert(i, val)
            i += 1
    return arr