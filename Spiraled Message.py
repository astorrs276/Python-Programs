def find_center(string, rows, cols):
    return string[(rows * cols) % len(string) - 1]