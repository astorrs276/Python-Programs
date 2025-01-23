def solve(s):
    open = []
    for char in s:
        if char == "(" or char == "[" or char == "{":
            open.append(char)
        elif char == ")":
            if open[-1] == "(":
                open.pop(-1)
            else:
                return False
        elif char == "]":
            if open[-1] == "[":
                open.pop(-1)
            else:
                return False
        elif char == "}":
            if open[-1] == "{":
                open.pop(-1)
            else:
                return False
    if len(open) > 0:
        return False
    else:
        return True