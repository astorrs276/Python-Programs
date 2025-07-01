def fibonacci(a, b):
    if b > 4000000:
        if b % 2 == 0:
            return b
        return 0
    val = fibonacci(b, a + b)
    if b % 2 == 0:
        return val + b
    return val

print(fibonacci(1, 1))