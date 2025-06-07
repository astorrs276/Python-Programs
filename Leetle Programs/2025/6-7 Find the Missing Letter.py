def solve(letters):
    return chr(ord(letters[-1]) - sum([ord(letters[i]) - ord(letters[0]) - i for i in range(len(letters))]))