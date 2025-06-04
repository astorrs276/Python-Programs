def solve(strs):
    anagrams = dict()
    for str in strs:
        ordered = "".join(sorted(str))
        if ordered not in anagrams:
            anagrams[ordered] = []
        anagrams[ordered].append(str)
    final = []
    for key in anagrams:
        final.append(anagrams[key])
    return final