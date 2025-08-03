def solve(words):
    first = sorted([word[0] for word in words])
    last = sorted([word[-1] for word in words])
    for i in range(len(first)):
        for j in range(len(last)):
            if first[:i] + first[i + 1:] == last[:j] + last[j + 1:]:
                return True
    return words == []