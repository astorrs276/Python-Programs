def solve(limit, number):
    return [str(number) + " x " + str(i) + " = " + str(number * i) for i in range(1, limit + 1)]