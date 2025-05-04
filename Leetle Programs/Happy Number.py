def solve(n):
    if n <= 0:
        return False
    checked = set()
    while n != 1 and n not in checked:
        checked.add(n)
        n = sum([(int(char) ** 2) for char in str(n)])
    return n == 1