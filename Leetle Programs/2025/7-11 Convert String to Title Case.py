def solve(s):
    return " ".join(["".join(list(word) if word[0].isdigit() else [chr(ord(list(word)[0]) - 32)] + list(word)[1:]) for word in s.lower().split()])