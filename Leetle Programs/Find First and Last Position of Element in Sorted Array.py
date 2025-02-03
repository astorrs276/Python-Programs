def solve(nums, target):
    pos = [-1, -1]
    for i in range(len(nums)):
        if nums[i] == target:
            if pos[0] == -1:
                pos = [i, i]
            else:
                pos[1] = i
    return pos