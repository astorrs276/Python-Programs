def solve(nums):
    running = True
    while running:
        running = False
        for i in range(len(nums) - 1):
                if (nums[i + 1] < nums[i]):
                        running = True
                        temp = nums[i]
                        nums[i] = nums[i + 1]
                        nums[i + 1] = temp
    while True:
        if nums[0] < 1:
            nums.pop(0)
        else:
            break
    j = 0
    while j < len(nums) - 1:
        if nums[j] == nums[j + 1]:
            nums.pop(j)
        else:
            j += 1
    for i, char in enumerate(nums):
        if char != (i + 1):
            return i + 1
    return len(nums) + 1