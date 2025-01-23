def solve(s):
    letters = []
    for char in s:
        ascii = ord(char)
        if 65 <= ascii <= 90:
            ascii += 32
            letters.append(chr(ascii))
        elif 48 <= ascii <= 57 or 97 <= ascii <= 122:
            letters.append(chr(ascii))
    for i in range(len(letters)):
        if letters[i] != letters[len(letters) - 1 - i]:
            return False
    return True