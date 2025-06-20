def solve(s):
    result = {'vowels': 0, 'consonants': 0, 'digits': 0, 'spaces': 0}
    for char in s.lower():
        if char.isdigit():
            result['digits'] += 1
        elif char in "aeiou":
            result['vowels'] += 1
        elif char == " ":
            result['spaces'] += 1
        elif char.isalpha():
            result['consonants'] += 1
    return result