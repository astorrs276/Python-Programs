def solve(strs):
    str = ""
    i = 0
    while True:
        i += 1
        if i > min([len(s) for s in strs]):
            break
        prefixes = set(strs[j][:i] for j in range(len(strs)))
        if len(prefixes) != 1:
            break
    return strs[0][:i - 1]