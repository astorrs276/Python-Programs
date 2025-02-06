def solve(n):
    if n == 0 or n == 1:
        return 0
    primes = []
    for i in range(2, n):
        broken = False
        for item in primes:
            if i % item == 0:
                broken = True
                break
        if not broken:
            primes.append(i)
    return len(primes)