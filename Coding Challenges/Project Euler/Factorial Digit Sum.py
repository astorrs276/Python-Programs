num = 1
for i in range(1, 101):
    num *= i
strung = str(num)

nums = [int(strung[i]) for i in range(len(strung))]

print(sum(nums))