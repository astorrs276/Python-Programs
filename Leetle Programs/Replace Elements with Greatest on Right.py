def solve(arr):
    if len(arr) == 0:
        return arr
    for i in range(len(arr) - 1):
        max = arr[i + 1]
        maxIndex = i + 1
        for j in range(i + 1, len(arr)):
            if arr[j] > max:
                max = arr[j]
                maxIndex = j
        arr[i] = arr[maxIndex]
    arr[-1] = -1
    return arr