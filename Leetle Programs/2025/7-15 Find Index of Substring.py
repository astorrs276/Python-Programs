def solve(pattern, text):
    return 0 if pattern == "" else len(text.split(pattern)[0]) if pattern in text else -1