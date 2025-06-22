def solve(arr):
    return len(arr) == 1 or len(set([sorted(arr)[i + 1] - sorted(arr)[i] for i in range(len(arr) - 1)])) == 1