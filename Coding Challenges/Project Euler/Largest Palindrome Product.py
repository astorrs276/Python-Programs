palindromes = []
for i in range(100, 1000):
    for j in range(100, 1000):
        if int(str(i * j)[::-1]) == (i * j):
            palindromes.append((i * j))

print(max(palindromes))