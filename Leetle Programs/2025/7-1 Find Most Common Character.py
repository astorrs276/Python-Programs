def solve(s):
    letters = dict()
    for char in s:
        letters[char] = letters.get(char, 0) + 1
    peak = ""
    for key in letters:
        if letters[key] > letters.get(peak, 0):
            peak = key
    return peak