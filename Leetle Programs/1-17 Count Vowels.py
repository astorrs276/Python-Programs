def solve(text):
    return sum([1 if char in "aeiou" else 0 for char in text.lower()])