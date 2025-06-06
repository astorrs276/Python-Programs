def hash(string):
    val = 1
    map = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26, "a": -1, "b": -2, "c": -3, "d": -4, "e": -5, "f": -6, "g": -7, "h": -8, "i": -9, "j": -10, "k": -11, "l": -12, "m": -13, "n": -14, "o": -15, "p": -16, "q": -17, "r": -18, "s": -19, "t": -20, "u": -21, "v": -22, "w": -23, "x": -24, "y": -25, "z": -26}
    for i in range(len(string) - 1):
        val *= (map[string[i]] + map[string[i + 1]])
    val = str(abs(val))
    while len(val) > 6:
        val = val[1:]
    while len(val) < 6:
        val = "0" + val
    return val

print(hash("BobCat")) # 009282
print(hash("BOOMer")) # 627520
print(hash("QuinnipiacUniversity")) # 000000
print(hash("ExAmPlEstRIng")) # 326720