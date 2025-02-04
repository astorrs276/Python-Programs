num = 1
for i in range(1, 21):
    n = i
    testNum = num
    j = 2
    while j <= n:
        if n % j != 0:
            j += 1
        else:
            if testNum % j == 0:
                testNum //= j
                n //= j
            else:
                num *= j
                n //= j

print(num)