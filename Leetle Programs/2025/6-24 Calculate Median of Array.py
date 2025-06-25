def solve(nums):
    return sorted(nums)[len(nums) // 2] if len(nums) % 2 == 1 else (sorted(nums)[len(nums) // 2 - 1] + sorted(nums)[len(nums) // 2]) / 2