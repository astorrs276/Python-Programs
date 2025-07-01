def collatz(num):
    count = 0
    while num != 1:
        count += 1
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
    return count

max = 0
maxNum = 0

for i in range(1, 1000000):
    if i % 10000 == 0:
        print(i)
    num = collatz(i)
    if num > max:
        max = num
        maxNum = i

print(maxNum)