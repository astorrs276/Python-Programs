def solve(dividend, divisor):
    if divisor == 0:
        raise(ZeroDivisionError)
    negative = (dividend < 0) ^ (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    count = 0
    while dividend >= divisor:
        dividend -= divisor
        count += 1
    return -count if negative else count