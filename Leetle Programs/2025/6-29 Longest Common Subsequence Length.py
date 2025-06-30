from itertools import combinations
def solve(text1, text2):
    for i in range(min(len(text1), len(text2)), 0, -1):
        for item in combinations(text1, i):
            item = list(item)
            for char in text2:
                if char == item[0]:
                    item.pop(0)
                    if len(item) == 0:
                        return i
    return 0