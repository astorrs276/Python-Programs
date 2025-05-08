def solve(nums, target):
    start = 0
    end = len(nums) - 1
    mid = (start + end) // 2
    while target != nums[mid]:
        if start == end:
            return -1
        elif target > nums[mid]:
            start = mid + 1
            mid = (start + end) // 2
        elif target < nums[mid]:
            end = mid
            mid = (start + end) // 2
    return mid