def solve(operations):
    vals = []
    result = []
    for op in operations:
        if op[0] == "push":
            vals.append(op[1])
            result.append(None)
        elif op[0] == "top":
            if len(vals) > 0:
                result.append(vals[-1])
        elif op[0] == "empty":
            result.append(len(vals) == 0)
        elif op[0] == "pop":
            if len(vals) > 0:
                result.append(vals.pop(-1))
    return result