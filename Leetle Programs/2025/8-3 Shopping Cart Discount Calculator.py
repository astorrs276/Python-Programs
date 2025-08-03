def solve(items):
    price = 0
    for item in items:
        if item[1] >= 3:
            item[1] = item[1] - item[1] // 3
        price += item[0] * item[1]
    if price > 100:
        if price >= 200:
            price = price * .9 - 20
        else:
            price *= .9
    return price