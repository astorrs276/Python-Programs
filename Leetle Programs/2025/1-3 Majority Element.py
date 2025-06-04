def solve(nums):
    numDict = dict()
    for item in nums:
        if item not in numDict:
            numDict[item] = 0
        numDict[item] += 1
    found = []
    for key in numDict:
        if numDict[key] > len(nums) / 2:
            return key