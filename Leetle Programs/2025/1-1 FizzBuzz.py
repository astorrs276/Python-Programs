def solve(n):
    return ["FizzBuzz" if i % 15 == 0 else "Buzz" if i % 5 == 0 else "Fizz" if i % 3 == 0 else i for i in range(1, n + 1)]