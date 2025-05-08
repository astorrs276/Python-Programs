def solve(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in text:
        if char.lower() in vowels:
            count += 1
    return count