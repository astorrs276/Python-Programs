def solve(n):
    nums = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            nums.append("FizzBuzz")
        elif i % 5 == 0:
            nums.append("Buzz")
        elif i % 3 == 0:
            nums.append("Fizz")
        else:
            nums.append(i)
    return nums