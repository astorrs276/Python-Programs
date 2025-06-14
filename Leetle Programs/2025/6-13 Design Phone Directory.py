def solve(n, operations):
    open = [i for i in range(n)]
    result = []
    for op in operations:
        if op[0] == "get":
            if len(open) > 0:
                result.append(open.pop(0))
            else:
                result.append(-1)
        elif op[0] == "check":
            result.append(op[1] in open)
        elif op[0] == "release":
            result.append(None)
            if op[1] not in open:
                open = sorted(open + [op[1]])
    return result