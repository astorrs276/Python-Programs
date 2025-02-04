factors = []
i = 2
n = 600851475143
while i**2 < 600851475143:
    if n % i == 0:
        n //= i
        factors.append(i)
    else:
        i += 1

print(max(factors))