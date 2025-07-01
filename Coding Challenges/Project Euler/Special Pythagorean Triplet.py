stop = False
for i in range(1, 999):
    if stop:
        break
    for j in range(1, 999):
        if i + j < 1000:
            k = 1000 - i - j
            if i ** 2 + j ** 2 == k ** 2:
                stop = True
                print(i * j * k)
                break