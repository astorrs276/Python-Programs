def solve(nums):
    if len(nums) > 0:
        nums = sorted(nums)
        newNums = []
        for item in nums:
            if item not in newNums:
                newNums.append(item)
        last = newNums.pop(0)
        lengths = []
        length = 1
        for num in newNums:
            if num == last + 1:
                last = num
                length += 1
            else:
                lengths.append(length)
                length = 1
                last = num
        lengths.append(length)
        return max(lengths)
    else:
        return 0