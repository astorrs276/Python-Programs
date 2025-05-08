def solve(nums):
    newNums = nums[:]
    i = 0
    changed = []
    while i < len(nums):
        min = float('inf')
        minIndexes = [-1]
        for j in range(len(nums)):
            if j in changed:
                continue
            if nums[j] < min:
                min = nums[j]
                minIndexes = [j]
            elif nums[j] == min:
                minIndexes.append(j)
        for index in minIndexes:
            newNums[index] = i
            changed.append(index)
        i += len(minIndexes)
    return newNums