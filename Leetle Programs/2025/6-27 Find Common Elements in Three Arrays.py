def solve(arr1, arr2, arr3):
    return sorted([item for item in arr1 if item in arr2 and item in arr3])