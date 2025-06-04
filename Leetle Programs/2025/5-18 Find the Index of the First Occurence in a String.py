def solve(haystack, needle):
    if needle == "":
        return 0
    most = len(haystack.split(needle))
    if most == 1:
        return -1
    for i in range(len(haystack)):
        if len(haystack[i:].split(needle)) != most:
            return i - 1
    return len(haystack) - 1