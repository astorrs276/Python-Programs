def solve(s):
    return sum(1 if char.isalpha() and char not in "aeiou" else 0 for char in s.lower())