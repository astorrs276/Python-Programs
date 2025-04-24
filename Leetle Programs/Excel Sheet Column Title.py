def solve(n):
    n -= 1
    result = ""
    while n >= 0:
        result = chr(65 + n % 26) + result
        n = n // 26 - 1
    if n == 0:
        return result
    return result