num1 = 0
num2 = 0

for i in range(1, 101):
    num1 += i
    num2 += i**2
num1 = num1 ** 2

print(num1 - num2)