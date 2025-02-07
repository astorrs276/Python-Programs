num = 2 ** 1000
strung = str(num)

nums = [int(strung[i]) for i in range(len(strung))]

print(sum(nums))