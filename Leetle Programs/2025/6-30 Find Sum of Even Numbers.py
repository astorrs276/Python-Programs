def solve(nums):
    return sum([num if num % 2 == 0 else 0 for num in nums])