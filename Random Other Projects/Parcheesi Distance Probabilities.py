def weak_doubles():
    chances = {}
    combo_sums = {}
    for i in range(1, 7):
        for j in range(1, 7):
            combo_sums[i + j] = combo_sums.get(i + j, []) + [(i, j)]
    for i in range(1, 13):
        combos = set()
        if i <= 6:
            for j in range(1, 7):
                combos.add((i, j))
                combos.add((j, i))
        for item in combo_sums.get(i, []):
            combos.add(item)
        chances[i] = len(combos)
    for key in chances:
        print(("" if key >= 10 else " ") + str(key) + ": " + ("" if chances[key] >= 10 else " ") + str(chances[key]) + "/36", sep="", end="")
        if key % 6 == 0:
            print()
        else:
            print(",  ", end="")

def strong_doubles():
    chances = {}
    combo_sums = {}
    for i in range(1, 7):
        for j in range(1, 7):
            combo_sums[i + j] = combo_sums.get(i + j, []) + [(i, j)]
            if i == j:
                combo_sums[7 - i] = combo_sums.get(7 - i, []) + [(i, j)]
                combo_sums[7] = combo_sums.get(7, []) + [(i, j)]
                combo_sums[(7 - i) * 2] = combo_sums.get((7 - i) * 2, []) + [(i, j)]
                combo_sums[14] = combo_sums.get(14, []) + [(i, j)]
                combo_sums[(7 - i) * 2 + i] = combo_sums.get((7 - i) * 2 + i, []) + [(i, j)]
                combo_sums[(7 - i) + 2 * i] = combo_sums.get((7 - i) + 2 * i, []) + [(i, j)]
    for i in range(1, 15):
        combos = set()
        if i <= 6:
            for j in range(1, 7):
                combos.add((i, j))
                combos.add((j, i))
        for item in combo_sums.get(i, []):
            combos.add(item)
        chances[i] = len(combos)
    for key in chances:
        print(("" if key >= 10 else " ") + str(key) + ": " + ("" if chances[key] >= 10 else " ") + str(chances[key]) + "/36", sep="", end="")
        if key % 7 == 0:
            print()
        else:
            print(",  ", end="")

def main():
    weak_doubles()
    print()
    strong_doubles()

if __name__ == "__main__":
    main()