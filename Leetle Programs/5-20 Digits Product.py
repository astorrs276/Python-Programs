def solve(product):
    if product == 0:
        return 10
    elif product == 1:
        return 1
    digits = []
    for i in range(9, 1, -1):
        while product % i == 0:
            product //= i
            digits.append(i)
    if product != 1:
        return -1
    return int(''.join(map(str, sorted(digits))))