def solve(num):
    start = num
    if num == 0:
        return True
    elif num % 10 == 0:
        return False
    n = 0
    while 10**n < num:
        n += 1
    new = 0
    for i in range(n):
        temp = start // (10**(n - i - 1))
        start = start % (10**(n - i - 1))
        new += temp * 10**i
    if num == new:
        return True
    else:
        return False