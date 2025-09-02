def solve(arr):
    max_len = 0
    for i in range(len(arr) - 2):
        pos = i
        while pos < len(arr) - 2:
            if arr[pos + 1] > arr[pos]:
                pos += 1
            else:
                break
        if arr[pos + 1] >= arr[pos]:
            break
        while pos < len(arr) - 1:
            if arr[pos + 1] < arr[pos]:
                pos += 1
            else:
                break
        max_len = max(max_len, pos - i + 1)
    return max_len